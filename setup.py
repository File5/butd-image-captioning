from setuptools import setup, find_packages

__version__ = '0.0.1'

exclude_dirs = ['bottom-up_features', 'nlg-eval-master']

setup(name='butd_image_captioning',
      version=__version__,
      description='Bottom-up Top-down image captioning model with PyTorch',
      author='Victor Milewski, Marie-Francine Moens, Iacer Calixto',
      packages=find_packages('.', exclude=exclude_dirs),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
      ],
      install_requires=['tqdm', 'dgl', 'numpy'],
)
