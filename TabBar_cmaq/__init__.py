import os
import streamlit.components.v1 as components
from dataclasses import dataclass
from typing import List

if True:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend", "build")
    print(build_path)
    _component_func = components.declare_component("tab_bar", path=build_path)
else:
    _component_func = components.declare_component("tab_bar", url="http://localhost:3000")


@dataclass(frozen=True, order=True, unsafe_hash=True)
class TabBarItemData:
    id: int
    title: str
    description: str

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}


def tab_bar(data: List[TabBarItemData], default=None, return_type=str, key=None):
    data = list(map(lambda item: item.to_dict(), data))
    component_value = _component_func(data=data, selectedId=default, key=key, default=default)
    print(component_value)
    try:
        if return_type == str:
            return str(component_value)
        elif return_type == int:
            return int(component_value)
        elif return_type == float:
            return float(component_value)
    except:
        return component_value
