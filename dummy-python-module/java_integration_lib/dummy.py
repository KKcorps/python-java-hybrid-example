from java_integration_lib import find_modules
import subprocess


def foo_bar():
  jar_path = find_modules._find_dummy_java_module()
  output = subprocess.check_output(["java", "-cp", jar_path, "org.example.Main"])
  print(str(output))


if __name__ == "__main__":
  foo_bar()
