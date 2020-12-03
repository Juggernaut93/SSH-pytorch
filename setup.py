import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SSH-pytorch",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = {'SSH', 'SSH.model', 'SSH.model.dataset', 'SSH.model.nms', 'SSH.model.roi_data_layer', 'SSH.model.rpn', 'SSH.model.utils'},
    package_dir = {'SSH': '.', 'SSH.model': 'model', 'SSH.model.dataset': 'model/dataset', 'SSH.model.nms': 'model/nms', 'SSH.model.roi_data_layer': 'model/roi_data_layer', 'SSH.model.rpn': 'model/rpn', 'SSH.model.utils': 'model/utils'},
    python_requires='>=3.6',
    data_files = [
                    ('SSH/check_point', ['check_point/check_point.zip']),
                    ('SSH/model/nms', [
                        'model/nms/cpu_nms.cpython-35m-x86_64-linux-gnu.so',
                        'model/nms/cpu_nms.cpython-37m-x86_64-linux-gnu.so',
                        'model/nms/gpu_nms.cpython-35m-x86_64-linux-gnu.so',
                        'model/nms/gpu_nms.cpython-37m-x86_64-linux-gnu.so'
                    ]),
                    ('SSH/model/utils/', ['model/utils/cython_bbox.cpython-37m-x86_64-linux-gnu.so'])
                 ]
)