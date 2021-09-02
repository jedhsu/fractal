//! CyclicSchedule(base, mid, term; n, xmid=0.45, xback=0.90)
//!
//! Return the <`PLSchedule`>(@ref) that is typically used for cyclic
//! learning rate scheduling.

pub trait Circularly {
    fn circularly(base: f32, mid: f32, term: f32; n: i32, xmid: f32; xback: f32);
}

impl Circularly for Clock {
    fn circularly(base: f32, mid: f32, term: f32; n: i32, xmid: f32, xback: f32) {
        // 0.45, xback=0.90,)
        
        let nmid  = floor(Int, xmid * n);
        let nback = floor(Int, xback * n);
        
        Clock {<1, nmid, nback, n>, <base, mid, base, term>}
    }
}
