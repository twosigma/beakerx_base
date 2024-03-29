# Copyright 2017 TWO SIGMA OPEN SOURCE, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import types
from IPython.display import display
from ipywidgets import Box, DOMWidget, Text, Label, Textarea, Password, Button, Widget, SelectMultiple, Select, \
    Dropdown, Checkbox, HBox, VBox, RadioButtons, Layout, widget_serialization, HTML
from ipywidgets.widgets.trait_types import InstanceDict
from traitlets import Int, Unicode, Dict, Bool, Union, List, Any


class EasyFormComponent:
    def __init__(self):
        self.onInitListeners = list()
        self.onChangeListeners = list()

    def onInit(self, f):
        if f is not None and isinstance(f, types.FunctionType):
            self.onInitListeners.append(f)
        return self

    def onChange(self, f):
        if f is not None and isinstance(f, types.FunctionType):
            self.onChangeListeners.append(f)
        return self

    def fireInit(self):
        for f in self.onInitListeners:
            f()

    def fireChanged(self, x=None):
        for f in self.onChangeListeners:
            f(x)

    def set_value(self, new_value):
        self.value = new_value

    def add_interface_to(target):
        target.onInitListeners = list()
        target.onChangeListeners = list()
        target.onInit = types.MethodType(EasyFormComponent.onInit, target)
        target.onChange = types.MethodType(EasyFormComponent.onChange, target)
        target.fireInit = types.MethodType(EasyFormComponent.fireInit, target)
        target.fireChanged = types.MethodType(EasyFormComponent.fireChanged, target)
        target.set_value = types.MethodType(EasyFormComponent.set_value, target)


class BeakerxLayout(Layout):
    _view_module = Unicode('@jupyter-widgets/base').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/base').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    def __init__(self, **kwargs):
        super(BeakerxLayout, self).__init__(**kwargs)


class BeakerxWidget(Widget):
    def __init__(self, **kwargs):
        super(BeakerxWidget, self).__init__(**kwargs)


class BeakerxDOMWidget(DOMWidget):
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)
    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)

    def __init__(self, **kwargs):
        super(BeakerxDOMWidget, self).__init__(**kwargs)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)


class BeakerxBox(Box):
    def __init__(self, **kwargs):
        super(BeakerxBox, self).__init__(**kwargs)
        self.components = dict()

    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)

    def _repr_mimebundle_(self, **kwargs):
        for component in self.components:
            self.components[component].fireInit()
        
        return super(BeakerxBox, self)._repr_mimebundle_(**kwargs)


class BeakerxTextArea(Textarea, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxTextArea, self).__init__(**kwargs)

    _model_name = Unicode('TextAreaModel').tag(sync=True)
    _view_name = Unicode('TextAreaView').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    cols = Int(default_value=-1).tag(sync=True)
    rows = Int(default_value=-1).tag(sync=True)
    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxText(Text, EasyFormComponent):
    def on_value_change(self, change):
        self.fireChanged(change['new'])

    def __init__(self, **kwargs):
        super(BeakerxText, self).__init__(**kwargs)
        self.observe(self.on_value_change, names='value')

    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    size = Int(default_value=-1).tag(sync=True)
    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxPassword(Password, EasyFormComponent):
    def on_value_change(self, change):
        self.fireChanged(change['new'])

    def __init__(self, **kwargs):
        super(BeakerxPassword, self).__init__(**kwargs)
        self.observe(self.on_value_change, names='value')

    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    size = Int(default_value=-1).tag(sync=True)
    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxHTML(HTML, EasyFormComponent):
    def __init__(self, *args, **kwargs):
        super(BeakerxHTML, self).__init__(**kwargs)
        if len(args) > 0:
            self.value = args[0]

    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxHTMLPre(HTML, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxHTMLPre, self).__init__(**kwargs)

    _view_name = Unicode('HTMLPreView').tag(sync=True)
    _model_name = Unicode('HTMLPreModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxButton(Button, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxButton, self).__init__(**kwargs)

    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)
    align_self = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None

    def actionPerformed(self, *args, **kwargs):
        pass


class BeakerxComboBox(Dropdown, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxComboBox, self).__init__(**kwargs)

    _view_name = Unicode('ComboBoxView').tag(sync=True)
    _model_name = Unicode('ComboBoxModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)
    editable = Bool(default_value=False).tag(sync=True)
    value = Any(None, allow_none=True).tag(sync=True)
    original_options = Union([List(), Dict()])
    style = None

    def _update_options_list(self, new_value):
        if new_value not in self.options:
            self.options = self.original_options[:]
            self.options += (new_value,)
            self._options_values = tuple(tuple(self.options))

    def _handle_msg(self, msg):
        if 'value' in msg['content']['data']['state']:
            value = msg['content']['data']['state']['value']
            self._update_options_list(value)
            self.value = value
        super(BeakerxComboBox, self)._handle_msg(msg)

    def set_value(self, value):
        if self.editable:
            self._update_options_list(value)
        self.value = value


class BeakerxCheckbox(Checkbox, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxCheckbox, self).__init__(**kwargs)

    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxCheckboxGroup(EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxCheckboxGroup, self).__init__(**kwargs)
        self.children = []

    def __set_value(self, new_value):
        for item in self.children:
            item.value = item.description in new_value

    value = property(lambda self: [item.description for item in self.children if item.value], __set_value)

    def addChildren(self, children):
        self.children.append(children)


class BeakerxLabel(Label, EasyFormComponent):
    def __init__(self, **kwargs):
        super(BeakerxLabel, self).__init__(**kwargs)

    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxHBox(HBox):
    def __init__(self, children=None, **kwargs):
        super(BeakerxHBox, self).__init__(**kwargs)
        if children is not None:
            self.children += tuple(children)

    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class BeakerxVBox(VBox):
    def __init__(self, **kwargs):
        super(BeakerxVBox, self).__init__(**kwargs)

    _view_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module = Unicode('@jupyter-widgets/controls').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    layout = InstanceDict(BeakerxLayout).tag(sync=True, **widget_serialization)
    style = None


class CyclingDisplayBox(BeakerxBox):
    _view_name = Unicode('CyclingDisplayBoxView').tag(sync=True)
    _model_name = Unicode('CyclingDisplayBoxModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)

    period = Int(5000).tag(sync=True)

    def __init__(self, children):
        super(CyclingDisplayBox, self).__init__()
        self.children += tuple(children)

    def setPeriod(self, period):
        self.period = period


class GridView(BeakerxVBox):
    _view_name = Unicode('GridView').tag(sync=True)
    _model_name = Unicode('GridViewModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)

    def __init__(self, rows):
        super(GridView, self).__init__()
        self.children += tuple(rows)


class SelectionContainer(BeakerxBox):
    _titles = Dict().tag(sync=True)

    def __init__(self, childrens, labels):
        super(SelectionContainer, self).__init__()
        labels_dict = dict()
        for x in labels:
            labels_dict[len(labels_dict)] = x
        self._titles = labels_dict
        self.children += tuple(childrens)


class Tab(SelectionContainer):
    _view_name = Unicode('TabView').tag(sync=True)
    _model_name = Unicode('TabModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)

    def __init__(self, childrens, labels):
        super(Tab, self).__init__(childrens, labels)


class SelectMultipleWithRows(SelectMultiple, EasyFormComponent):
    def __init__(self, **kwargs):
        super(SelectMultipleWithRows, self).__init__(**kwargs)

    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)
    size = Int(5, help="The number of rows to display.").tag(sync=True)


class SelectMultipleSingle(Select, EasyFormComponent):
    def __init__(self, **kwargs):
        super(SelectMultipleSingle, self).__init__(**kwargs)

    _view_name = Unicode('SelectMultipleSingleView').tag(sync=True)
    _model_name = Unicode('SelectMultipleSingleModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)
    size = Int(5, help="The number of rows to display.").tag(sync=True)


class RadioButtons(RadioButtons, EasyFormComponent):
    def __init__(self, **kwargs):
        super(RadioButtons, self).__init__(**kwargs)


class DatePicker(BeakerxDOMWidget, EasyFormComponent):
    def __init__(self, value=None, **kwargs):
        if value is not None:
            kwargs['value'] = value
        super(DatePicker, self).__init__(**kwargs)

    _view_name = Unicode('DatePickerView').tag(sync=True)
    _model_name = Unicode('DatePickerModel').tag(sync=True)
    _view_module = Unicode('beakerx').tag(sync=True)
    _model_module = Unicode('beakerx').tag(sync=True)
    _model_module_version = Unicode('*').tag(sync=True)
    _view_module_version = Unicode('*').tag(sync=True)

    showTime = Bool(default_value=False,
                    help="Enable or disable user changes.").tag(sync=True)
    value = Unicode(default_value="").tag(sync=True)
    description = Unicode(default_value="").tag(sync=True)
