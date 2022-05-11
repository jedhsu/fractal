use std::op::{Add, Subtract, Multiply};

pub struct Quaternion {
    s: f64,
    v1: f64,
    v2: f64,
    v3: f64,
}

// q = quaternion()                 object initialization
// q = quaternion(s, v1, v2, v3)    from 4 elements
impl Quaternion {
    fn from_coords(arg1: f64, arg2: f64, arg3: f64, arg4: f64,):
        self.vec = [];
        if args.len() == 0 {
        } else if len(args) == 4 {
            let self.s = args[0];
            let self.v = mat(args[1:4]);
        } else {
            print("error")
            return None
        }

}

    fn from_homogeneous(self, t: Homogeneous) {
        qs = sqrt(trace(t)+1)/2.0
        kx = t[2,1] - t[1,2]    # Oz - Ay
        ky = t[0,2] - t[2,0]    # Ax - Nz
        kz = t[1,0] - t[0,1]    # Ny - Ox
    }

        if (t[0,0] >= t[1,1]) and (t[0,0] >= t[2,2]) {
                kx1 = t[0,0] - t[1,1] - t[2,2] + 1      # Nx - Oy - Az + 1
                ky1 = t[1,0] + t[0,1]           # Ny + Ox
                kz1 = t[2,0] + t[0,2]           # Nz + Ax
                add = (kx >= 0)
        } elif (t[1,1] >= t[2,2]) {
                kx1 = t[1,0] + t[0,1]           # Ny + Ox
                ky1 = t[1,1] - t[0,0] - t[2,2] + 1  # Oy - Nx - Az + 1
                kz1 = t[2,1] + t[1,2]           # Oz + Ay
                add = (ky >= 0)
        } else {
                kx1 = t[2,0] + t[0,2]           # Nz + Ax
                ky1 = t[2,1] + t[1,2]           # Oz + Ay
                kz1 = t[2,2] - t[0,0] - t[1,1] + 1  # Az - Nx - Oy + 1
                add = (kz >= 0)

        if add {
                kx = kx + kx1
                ky = ky + ky1
                kz = kz + kz1
        } else {
                kx = kx - kx1
                ky = ky - ky1
                kz = kz - kz1
        }

        kv = matrix([kx, ky, kz])
        nm = linalg.norm( kv )
        if self == 0():
                self.s = 1.0
                self.v = matrix([0.0, 0.0, 0.0])

        else:
                self.s = qs
                self.v = (sqrt(1 - qs**2) / nm) * kv
    }

}

'''
Return a new quaternion that is the element-wise difference of the operands.
'''
impl Add for Quaternion {
    fn add(self, q):
        if isinstance(q, quaternion) {
            qr = quaternion()
            qr.s = 0

            qr.s = self.s + q.s
            qr.v = self.v + q.v

            return qr
        else:
            raise ValueError
    fn __rmul__(self, c):
        qr = quaternion()
        qr.s = self.s * c
        qr.v = self.v * c

        return qr
        
    def __imul__(self, x):
        '''
        Quaternion in-place multiplication
        
            - q *= q2
            
        '''
        
        if isinstance(x, quaternion):
            s1 = self.s;   
            v1 = self.v
            s2 = x.s
            v2 = x.v

            # form the product
            self.s = s1*s2 - v1*v2.T
            self.v = s1*v2 + s2*v1 + cross(v1,v2)

        elif isscalar(x):
            self.s *= x;
            self.v *= x;

        return self;


    '''Return quaternion quotient.  Several cases handled
       - q1 / q2      quaternion division implemented as q1 * q2.inv()
       - q1 / c       element-wise division
       '''
    fn __div__(self, q) {
        if isinstance(q, quaternion) {
            let qr = quaternion()
            let qr = self * q.inv()
        } else if  isscalar(q) {
            let qr.s = self.s / q
            let qr.v = self.v / q
    
            return qr
        }
    }

    '''
    Quaternion exponentiation.  Only integer exponents are handled.  Negative
    integer exponents are supported.
    '''
    def __pow__(self, p):
        # check that exponent is an integer
        if not isinstance(p, int):
            raise ValueError
        
        qr = quaternion()
        q = quaternion(self);
        
        # multiply by itself so many times
        for i in range(0, abs(p)):
            qr *= q

        # if exponent was negative, invert it
        if p < 0:
            qr = qr.inv()

        return qr

    # def copy(self):
    #     """
    #     Return a copy of the quaternion.
    #     """
    #     return copy.copy(self);
    #
    # def inv(self):
    #     """Return the inverse.
    #
    #     @rtype: quaternion
    #     @return: the inverse
    #     """
    #
    #     qi = quaternion(self);
    #     qi.v = -qi.v;
    #
    #     return qi;
    #
    #
    #
    # def norm(self):
    #     """Return the norm of this quaternion.
    #
    #     @rtype: number
    #     @return: the norm
    #     """
    #
    #     return linalg.norm(self.double())
    #

    /// Return the quaternion as 4-element vector.
    fn double(self) -> <f64, f64, f64, f64> {
        return concatenate((mat(self.s), self.v), 1 );
    }
