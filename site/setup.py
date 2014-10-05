from setuptools import setup

setup(name='TwitSearch', version='1.0',
      description='Python2.7 app running on Bottle and Openshift',
      author='Laura Duggan', author_email='07314299@ucdconnect.ie',
      url='python-labhra.rhcloud.com',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                          'bottle',
                        'oauthlib',
                        'PyMySQL',
                        'python-twitter',
                        'requests',
                        'tweepy'
      ],
     )
