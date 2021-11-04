import os
import re
import sys

from setuptools import setup
from setuptools.command.develop import develop

try:
    import jupyter_core.paths as jupyter_core_paths
except Exception:
    jupyter_core_paths = None

ROOT = os.path.dirname(os.path.abspath(__file__))


class DevelopCmd(develop):
    prefix_targets = [
        ("nbconvert/templates", "lab_offline"),
        ("nbconvert/templates", "webpdf_offline"),
    ]

    def run(self):
        target_dir = os.path.join(sys.prefix, "share", "jupyter")
        if "--user" in sys.prefix:  # TODO: is there a better way to find out?
            target_dir = jupyter_core_paths.user_dir()
        target_dir = os.path.join(target_dir)

        for prefix_target, name in self.prefix_targets:
            source = os.path.join("share", "jupyter", prefix_target, name)
            target = os.path.join(target_dir, prefix_target, name)
            target_subdir = os.path.dirname(target)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)
            rel_source = os.path.relpath(
                os.path.abspath(source), os.path.abspath(target_subdir)
            )
            try:
                os.remove(target)
            except Exception:
                pass
            print(rel_source, "->", target)
            os.symlink(rel_source, target)

        super(DevelopCmd, self).run()


def patch_html_manager(embed_path: str, static_path: str) -> None:
    cdn = r"https:\/\/unpkg.com"
    embed_original = os.path.join(embed_path, "embed-amd-original.js")
    embed = os.path.join(embed_path, "embed-amd.js")

    with open(embed_original, "r") as f:
        content: str = f.read()
    with open(embed, "w") as f:
        pattern = fr"{cdn}\/@jupyter-widgets\/html-manager@(.*?)\/dist"
        new_content = re.sub(pattern, static_path, content)
        f.write(new_content)


static_prefix = os.path.join(
    "share",
    "jupyter",
    "nbconvert",
    "templates",
    "lab_offline",
    "static",
    "@jupyter-widgets",
    "html-manager@0.20.0",
    "dist",
)

embed_path = os.path.join(
    ROOT,
    static_prefix,
)

static_path = os.path.join(sys.prefix, static_prefix)
patch_html_manager(embed_path, static_path)

data_files = []

for root, dirs, files in os.walk("share"):
    if files:
        root_files = [
            os.path.join(root, i)
            for i in files
            if i != "embed-amd-original.js"
        ]
        data_files.append((root, root_files))


setup_args = dict(
    entry_points={
        "nbconvert.exporters": [
            "html-offline = nb_offline_convert:OfflineHTMLExporter",
            "webpdf-offline = nb_offline_convert:OfflineWebPDFExporter"
        ],
    },
    data_files=data_files,
    cmdclass={
        "develop": DevelopCmd,
    }
    if jupyter_core_paths
    else {},
)

setup(**setup_args)
