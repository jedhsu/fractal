"""

    *Now*

"""


fn now():
    eps = 1e-16
    dummy_loss = Time.Loss(
        0,
        0,
        0,
        0,
        0,
    )
    dummy_status = Report.LearningStatus(
        dummy_loss,
        0,
        0,
    )
    return Now.Learning(
        eps,
        eps,
        eps,
        eps,
        dummy_status,
        <>,
        <>,
        false,
    )