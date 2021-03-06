# -*- coding: utf-8 -*-
# Copyright 2007-2011 The Hyperspy developers
#
# This file is part of  Hyperspy.
#
#  Hyperspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  Hyperspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  Hyperspy.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup

import distutils.dir_util

import os
import sys
import shutil

import hyperspy.Release as Release
# clean the build directory so we aren't mixing Windows and Linux 
# installations carelessly.
if os.path.exists('build'):
    distutils.dir_util.remove_tree('build')

install_req = ['scipy', 'ipython', 'matplotlib', 'numpy', 'mdp',
'traits', 'traitsui', 'h5py', 'scikit_learn']

def are_we_building4windows():
    for arg in sys.argv:
        if 'wininst' in arg:
            return True
scripts = ['bin/hyperspy',]

if are_we_building4windows() or os.name in ['nt','dos']:
    # In the Windows command prompt we can't execute Python scripts 
    # without a .py extension. A solution is to create batch files
    # that runs the different scripts.
    # (code adapted from scitools)
    scripts.extend(('bin/win_post_installation.py',
                   'bin/install_hyperspy_here.py',
                   'bin/uninstall_hyperspy_here.py'))
    batch_files = []
    for script in scripts:
        batch_file = os.path.splitext(script)[0] + '.bat'
        f = open(batch_file, "w")
        f.write('set path=%~dp0;%~dp0\..\;%PATH%\n')
        if script == 'bin/hyperspy':
            f.write('start pythonw "%%~dp0\%s" --ipython_args qtconsole %%*\n' % os.path.split(script)[1])
        else:
            f.write('python "%%~dp0\%s" %%*\n' % os.path.split(script)[1])
        f.close()
        batch_files.append(batch_file)
    scripts.extend(batch_files)
    
version = Release.version
setup(
    name = "hyperspy",
    package_dir = {'hyperspy': 'hyperspy'},
    version = version,
    packages = ['hyperspy', 'hyperspy.components', 'hyperspy.io_plugins', 
                'hyperspy.drawing', 'hyperspy.learn', 'hyperspy.signals', 
                'hyperspy.gui', 'hyperspy.tests', 'hyperspy.models',
                'hyperspy.tests.io', 'hyperspy.misc', 'hyperspy.misc.mpfit', 
                'hyperspy.misc.mpfit.tests'],
    requires = install_req,
    scripts = scripts,
    package_data = 
    {
        'hyperspy': 
            [   'bin/*.py',
                'ipython_profile/*',
                'data/*.m', 
                'data/*.csv',
                'data/*.tar.gz',
				'data/hyperspy_logo.ico',
		'tests/io/dm3_1D_data/*.dm3',
		'tests/io/dm3_2D_data/*.dm3',
		'tests/io/dm3_3D_data/*.dm3',
            ],
    },
    author = Release.authors['all'][0],
    author_email = Release.authors['all'][1],
    maintainer = 'Francisco de la Peña',
    maintainer_email = 'fjd29@cam.ac.uk',
    description = Release.description,
    long_description = open('README.txt').read(),
    license = Release.license,
    platforms = Release.platforms,
    url = Release.url,
    #~ test_suite = 'nose.collector',
    keywords = Release.keywords,
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        ],
    )
