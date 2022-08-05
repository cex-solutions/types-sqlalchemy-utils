from .. import i18n as i18n
from ..utils import str_coercible as str_coercible


@str_coercible
class WeekDay:
    NUM_WEEK_DAYS: int

    def __init__(self, index: int) -> None:
        pass

    def get_name(self, width:str='wide', context:str='format') -> str:
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def position(self) -> int:
        pass