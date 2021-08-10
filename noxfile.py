"""

    *nox*

  Parameters for nox.

"""
import shutil
import sys
from pathlib import Path
from textwrap import dedent

import tempfile

import nox
from nox_poetry import Session
from nox_poetry import session


__package__ = "topos"
__versions__ = [
    "3.9",
    "3.8",
]

nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "pre-commit",
    "mypy",
    "typeguard",
    "security",
    "tests",
    "examples",
    "docs-build",
)


def install_with_constraints(
    session,
    *args,
    **kwargs,
):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(
            f"--constraint={requirements.name}",
            *args,
            **kwargs,
        )


"""

    *activate*

  Activates venv using precommit hooks.

"""


def activate(
    session: Session,
):
    if session.bin is None:
        return

    virtualenv = session.env.get("VIRTUAL_ENV")
    if virtualenv is None:
        return

    hookdir = Path(".git") / "hooks"
    if not hookdir.is_dir():
        return

    for hook in hookdir.iterdir():
        if hook.name.endswith(".sample") or not hook.is_file():
            continue

        text = hook.read_text()
        bindir = repr(session.bin)[1:-1]  # strip quotes
        if not (
            (Path("A") == Path("a") and bindir.lower() in text.lower())
            or (bindir in text),
        ):
            continue

        lines = text.splitlines()
        if not (lines[0].startswith("#!") and "python" in lines[0].lower()):
            continue

        header = dedent(
            f"""\
            import os
            os.environ["VIRTUAL_ENV"] = {virtualenv!r}
            os.environ["PATH"] = os.pathsep.join((
                {session.bin!r},
                os.environ.get("PATH", ""),
            ))
            """
        )

        lines.insert(1, header)
        hook.write_text("\n".join(lines))


"""

    *lint*

  Lint using pre-commit.

"""


@session(
    name="pre-commit",
    python="3.9",
)
def lint(
    session: Session,
):
    args = session.posargs or [
        "run",
        "--all-files",
        "--show-diff-on-failure",
    ]
    install_with_constraints(
        session,
        "pre-commit",
        "pre-commit-hooks",
        "black",
        "darglint",
        "flake8",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-rst-docstrings",
        "pep8-naming",
        "reorder-python-imports",
    )
    session.run("pre-commit", *args)
    if args and args[0] == "install":
        activate(session)


"""

    *static-types*

  Check for well-typedness through _mypy_.

"""


@session(
    python=__versions__,
)
def mypy(
    session: Session,
) -> None:
    args = session.posargs or [
        "src",
        "tests",
        "docs/conf.py",
    ]
    session.install(".")
    session.install(
        "mypy",
        "pytest",
    )
    session.run(
        "mypy",
        *args,
    )
    if not session.posargs:
        session.run(
            "mypy",
            f"--python-executable={sys.executable}",
            "noxfile.py",
        )


"""

    *runtime-types*

  Checks for type safety at runtime with _typeguard_.

"""


@session(
    python=__versions__,
)
def typeguard(
    session: Session,
):
    session.install(".")
    session.install(
        "pytest",
        "typeguard",
        "pygments",
    )
    session.run(
        "pytest",
        f"--typeguard-packages={__package__}",
        *session.posargs,
    )


"""

    *tests*

  Runs the test suite with _pytest_.

"""


@session(
    python=[
        "3.9",
        "3.8",
        "3.7",
    ]
)
def tests(
    session: Session,
) -> None:
    session.install(".")
    session.install(
        "coverage[toml]",
        "pytest",
        "pygments",
    )
    try:
        session.run(
            "coverage",
            "run",
            "--parallel",
            "-m",
            "pytest",
            *session.posargs,
        )
    finally:
        if session.interactive:
            session.notify(
                "coverage",
                posargs=[],
            )


"""

    *coverage*

  Analyzes code coverage with _coverage_.

"""


@session
def coverage(
    session: Session,
) -> None:
    args = session.posargs or ["report"]

    session.install("coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


"""

    *security*

  Scans dependencies for insecure packages through _safety_.

"""


@session(python="3.9")
def security(
    session: Session,
) -> None:
    requirements = session.poetry.export_requirements()
    session.install("safety")
    session.run(
        "safety",
        "check",
        "--full-report",
        f"--file={requirements}",
    )


"""

    *docs-build*

  Build the docs.

"""


@session(
    name="docs-build",
    python="3.9",
)
def docs_build(
    session: Session,
) -> None:
    """Build the documentation."""
    args = session.posargs or [
        "docs",
        "docs/_build",
    ]
    session.install(".")
    session.install(
        "sphinx",
        "sphinx-click",
        "sphinx-rtd-theme",
    )

    build_dir = Path(
        "docs",
        "_build",
    )
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run(
        "sphinx-build",
        *args,
    )


"""

    *build-with-view*

  Build and serve the documentation with live reloading on changes.

"""


@session(
    python="3.9",
)
def docs(
    session: Session,
) -> None:
    args = session.posargs or [
        "--open-browser",
        "docs",
        "docs/_build",
    ]

    session.install(".")
    session.install(
        "sphinx",
        "sphinx-autobuild",
        "sphinx-click",
        "sphinx-rtd-theme",
    )

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run(
        "sphinx-autobuild",
        *args,
    )


"""

    *examples*

  Run examples with xdoctest.

"""


@session(
    python=__versions__,
)
def examples(
    session: Session,
) -> None:
    args = session.posargs or ["all"]
    session.install(".")
    session.install("xdoctest[colors]")
    session.run(
        "python",
        "-m",
        "xdoctest",
        __package__,
        *args,
    )
