from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import deprecated

from ..cmd import Command

def show_formats() -> None: ...

class sdist(Command):
    description: ClassVar[str]

    def checking_metadata(self): ...

    user_options: Incomplete
    boolean_options: Incomplete
    help_options: Incomplete
    negative_opt: Incomplete
    READMES: Incomplete
    template: Incomplete
    manifest: Incomplete
    use_defaults: int
    prune: int
    manifest_only: int
    force_manifest: int
    formats: Incomplete
    keep_temp: int
    dist_dir: Incomplete
    archive_files: Incomplete
    metadata_check: int
    owner: Incomplete
    group: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    filelist: Incomplete
    def run(self) -> None: ...
    @deprecated("distutils.command.sdist.check_metadata is deprecated, use the check command instead")
    def check_metadata(self) -> None: ...
    def get_file_list(self) -> None: ...
    def add_defaults(self) -> None: ...
    def read_template(self) -> None: ...
    def prune_file_list(self) -> None: ...
    def write_manifest(self) -> None: ...
    def read_manifest(self) -> None: ...
    def make_release_tree(self, base_dir, files) -> None: ...
    def make_distribution(self) -> None: ...
    def get_archive_files(self): ...

def is_comment(line: str) -> bool: ...