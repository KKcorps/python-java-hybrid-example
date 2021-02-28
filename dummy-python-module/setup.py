from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from shutil import copytree, copy, rmtree
from setuptools import setup
import os
import sys
from distutils.command.build_ext import build_ext
import glob
from setuptools.command.install import install


class Install(install):
    def run(self):
        install.run(self)
        print("test.....")


def remove_if_exists(file_path):
    if os.path.exists(file_path):
        if os.path.islink(file_path) or os.path.isfile(file_path):
            os.remove(file_path)
        else:
            assert os.path.isdir(file_path)
            rmtree(file_path)


def find_file_path(pattern):
    files = glob.glob(pattern)
    if len(files) < 1:
        print("Failed to find the file %s." % pattern)
        exit(-1)
    if len(files) > 1:
        print("The file pattern %s is ambiguous: %s" % (pattern, files))
        exit(-1)
    return files[0]


current_dir = os.path.abspath(os.path.dirname(__file__))

JAR_PATH = "jars"

in_source_dir = os.path.isfile("../pom.xml")

try:
  if in_source_dir:
      try:
        os.mkdir(JAR_PATH)
      except:
        print("Jar path already exists {0}".format(JAR_PATH),
              file=sys.stderr)

      copy("../dummy-java-module/target/dummy-java-module-1.0-SNAPSHOT.jar", os.path.join(JAR_PATH, "dummy-java-module-1.0-SNAPSHOT.jar"))

      PACKAGES = ["java_integration_lib", "java_integration_lib.jars"]
      PACKAGE_DIR = {"java_integration_lib.jars" : "jars"}
      PACKAGE_DATA = {"java_integration_lib.jars" : ["*.jar"]}

      setup(
              name='java-integration-lib',
              version="1.0.0",
              packages=PACKAGES,
              include_package_data=True,
              package_dir=PACKAGE_DIR,
              package_data=PACKAGE_DATA,
              cmdclass={
                  'install': Install
              },
              scripts=[],
              author='Kartik Khare',
              author_email='kharekartik@gmail.com',
              description='Apache Flink Python API',
              python_requires='>=3.5',
              install_requires=[],
              zip_safe=False,
              classifiers=[
                  'Programming Language :: Python :: 3.8']
          )
finally:
    if in_source_dir:
      #print(in_source_dir)
      remove_if_exists(JAR_PATH)


