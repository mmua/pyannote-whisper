import os

from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#") and not line.startswith("-")
        ]


setup(
    name="pyannote-whisper",
    py_modules=["pyannote-whisper"],
    version="1.0",
    description="Speech Recognition plus diarization",
    readme="README.md",
    python_requires=">=3.9",
    author="Ruiqing",
    url="https://github.com/yinruiqing/pyannote-whisper",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        'console_scripts': ['pyannote-whisper=pyannote_whisper.cli.transcribe:cli'],
    },
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
