from cvt cimport *
from libcpp cimport bool

cdef extern from "../src/kcftracker.hpp":
	cdef cppclass KCFTracker:
		KCFTracker(bool, bool, bool, bool)
		void init(Rect, Mat)
		void update_(Rect, Mat, double)
		Rect predict(Mat)

		Rect update(Mat)

cdef class kcftracker:
	cdef KCFTracker *classptr
	
	def __cinit__(self, hog, fixed_window, multiscale, lab):
		self.classptr = new KCFTracker(hog, fixed_window, multiscale, lab)
		
	def __dealloc(self):
		del self.classptr
		
	def init(self, rectlist, ary):
		self.classptr.init(pylist2cvrect(rectlist), nparray2cvmat(ary))

	def update_(self, rectlist, ary, interp_factor):
		self.classptr.update_(pylist2cvrect(rectlist), nparray2cvmat(ary), interp_factor)

	def predict(self, ary):
		rect = self.classptr.predict(nparray2cvmat(ary))
		return cvrect2pylist(rect)
		
	def update(self, ary):
		rect = self.classptr.update(nparray2cvmat(ary))
		return cvrect2pylist(rect)
