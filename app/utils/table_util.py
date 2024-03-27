from app.db.main import (
    Thesis,
    TechnologyCategory,
    Account,
    Task,
    Group,
    Criterion,
    InterfaceDAO
)
from typing import *
from app.ui.base.base_ui import BaseUI
from app.custom.TableView import TableView

T_UI = TypeVar('T_UI', bound=BaseUI)

class TableUtil:
    base_ui: Generic[T_UI] = None
    table_ui: TableView = None
    func_format_data: Callable[[List[InterfaceDAO]], List[Dict[str, str]]] = None
    res_data = []
    state = 0

    @staticmethod
    def find_data(db_dao: InterfaceDAO, word_find: str) -> None:
        try: 
            word_find = word_find.lower()

            TableUtil.res_data = []
            for data in db_dao.get_all():
                convert_format_find = TableUtil.func_format_data([data])[1] if TableUtil.func_format_data([data]).__len__() > 1 else []
                
                # print(convert_format_find)
                join_values = ', '.join([str(value).lower() for value in convert_format_find])
                # print(f'Found data: {join_values}')

                if word_find in join_values and data not in TableUtil.res_data:
                    print('------------------------------ Result for searching data ------------------------------')
                    print(f'Found data: {join_values}')
                    TableUtil.res_data.append(data)

            if TableUtil.res_data.__len__() == 0:
                TableUtil.res_data = db_dao.get_all()

            # print('------------------------------ Result for searching data ------------------------------')
            print(f'Found data: {TableUtil.res_data}')
                    

            TableUtil.table_ui.update_values(TableUtil.func_format_data(TableUtil.res_data))

        except Exception as e:
            print(f'Error: {e}')
            TableUtil.table_ui.update_values(TableUtil.func_format_data(db_dao.get_all()))

