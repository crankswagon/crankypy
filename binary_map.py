"""
derp
"""

from dataclasses import dataclass

@dataclass
class ExecutionContext:
    """_summary_
    """
    is_live: bool = True
    is_clean_run: bool = True
    use_legacy_feed: bool = False

    def __post_init__(self):
        iota = 0
        for idx, ipt in enumerate(self.__dict__.keys()):
            if self.__getattribute__(ipt):
                iota += self.__getattribute__(ipt) * 2**idx
            else:
                iota = iota << 1
        self.settings = iota


def clean():
    """_summary_
    """
    print("clean up target destination")


def legacy_transform():
    """_summary_
    """
    print("execute some legacy logic")


def transform():
    """_summary_
    """
    print("execute some logic")


execution_playbook = {
    0b100: [transform],
    0b110: [clean, transform],
    0b101: [legacy_transform],
    0b111: [clean, legacy_transform],
}

run_context = ExecutionContext()
for f in execution_playbook[run_context.settings]:
    f()
