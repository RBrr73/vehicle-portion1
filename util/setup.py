# pylint: disable-msg=F0401

import os
import sys
import time
from setuptools import setup, find_packages

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here,
                                                 'src',
                                                 'oottadao',
                                                 'util routines')))

import releaseinfo
version = releaseinfo.__version__

setup(name='oottadao.util',
      version=version,
      description="various interim utility routines",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='http://oottadao.org',
      license='Apache License, Version 2.0',
      namespace_packages=["oottadao"],

      include_package_data=False,
      package_data={
          'oottadao.util.test': ['src/doubler.py']
      },
      test_suite='nose.collector',
      zip_safe=True,
      install_requires=[
          'setuptools',
          'pycrypto==2.3',
          'pyparsing',
          'zipapply',
          'Traits==4.3.0',
          #'PyYAML==3.09',
      ],
      entry_points="""
      [console_scripts]
      xyplot=oottadao.util.casedb:cmdlineXYplot
      plotgraph=oottadao.util.graphplot:main
      dotgraph=oottadao.util.dotgraph:main
      bargraph=oottadao.util.bargraph:main
      plotgraph=oottadao.util.plotgraph:main
      add_reqs=oottadao.util.addreqs:main
      mkpseudo=oottadao.util.mkpseudo:mkpseudo
      pottodump=pottodao.util.dep:mkpseudo
      envdump=oottadao.util.envirodump:envdump
      update_libpath=oottadao.util.lib:update_libpath
      combine_paths=oottadao.util.lib:combine_paths
      """
      )

kwds = {'install_requires':['numpy'],
        'version': '1.0.2',
        'zip_safe': False,
        'edit_time': True
        'license': 'public domain',
        'url': 'http://www.scilab.org/contrib/index_contrib.php?page=displayContribution&fileID=8562',
        'package_data': {'oottadao.main': ['*.html']},
        
        def install(dist):
    cmd = [sys.executable]
    if dist == "ready":
        cmd.append('oottadao.devtools/src/oottadao/files/devtools/conda_build3.py')
        cmd.append('dev')
    elif dist == "Virtualenv":
        cmd.append('go-oottadao-dev.py')
        
