from setuptools import setup
import os
version = '0.3.0dev'

if os.path.isdir('/home/pi/raspi-sump'):
    cmd = 'chown -R pi /home/pi/raspi-sump/'
    os.system(cmd)
    cmd = 'chmod 700 /home/pi/raspi-sump/raspisump.conf'
    os.system(cmd)
else:
    pass

raspi_sump_files = ['raspisump/raspisump.py',
                    'raspisump/raspisump_alternate.py',
                    'raspisump/todaychart.py',
                    'raspisump/checkpid.py'
                    ]

add_files = [('home/pi/raspi-sump', ['conf/raspisump.conf']),
             ('home/pi/raspi-sump/docs', ['docs/README.md']),
             ('home/pi/raspi-sump/docs', ['docs/automated_install.md']),
             ('home/pi/raspi-sump/docs', ['docs/manual_install.md'])
             ]

setup(name='raspisump',
      version=version,
      description='A sump pit monitoring system for Raspberry Pi',
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: End Users",
          "Natural Language :: English",
          "Operating System :: Raspbian Linux",
          "Programming Language :: Python :: 2.7",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      author='Al Audet',
      author_email='alaudet@linuxnorth.org',
      url='http://www.linuxnorth.org/raspi-sump/',
      download_url='https://github.com/alaudet/raspi-sump/releases',
      license='MIT License',
      scripts=raspi_sump_files,
      data_files=add_files,
      install_requires=['RPi.GPIO']
      )
