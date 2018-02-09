from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy
import subprocess
import os


python_root = subprocess.Popen("which python", shell=True, stdout=subprocess.PIPE
                               ).stdout.read().decode().strip()
print(python_root)
python_root = os.path.join(os.path.split(python_root)[0], '..')


libdr = ['/usr/local/lib']
incdr = [numpy.get_include(), '/usr/local/include/', os.path.join(python_root, 'include')]
# incdr = [numpy.get_include(), '/usr/local/include/', '/data/anaconda2/envs/py3/bin/../include']

ext = [
    Extension('cvt', ['python/cvt.pyx'],
              language='c++',
              extra_compile_args=['-std=c++11'],
              include_dirs=incdr,
              library_dirs=libdr,
              libraries=['opencv_core']),
    Extension('KCF', ['python/KCF.pyx', 'src/kcftracker.cpp', 'src/fhog.cpp'],
              language='c++',
              extra_compile_args=['-std=c++11'],
              include_dirs=incdr,
              library_dirs=libdr,
              libraries=['opencv_core', 'opencv_imgproc'])
]

setup(
    name='KCFcpp',
    version='0.0.1',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext
)

# python setup.py build_ext --inplace
