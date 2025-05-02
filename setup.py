from setuptools import setup, find_packages
setup(
    name = "sample-plugin-2",
    version = "1.0.0",
    description = "sample plugin 2",
    author = "Aathithya Sharan",
    packages = find_packages(),
    install_requires = [
        'PyQt5>=5.14.2',
    ],
    entry_points = {
        "osdag.plugins":[
            "sample_plugin2"= "sample_plugin_2:Action"
        ]
    },
    python_requires>=">=3.7",

)