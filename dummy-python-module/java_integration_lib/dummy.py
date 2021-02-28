from find_modules import _find_dummy_java_module
import subprocess


def foo_bar():
  jar_path = _find_dummy_java_module()
  output = subprocess.check_output(["java", "-cp", jar_path, "org.example.Main"])
  print(output)


if __name__ == "__main__":
  foo_bar()
