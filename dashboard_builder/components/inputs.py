# components/inputs.py

from flask import render_template_string

class BaseInput:
    def __init__(self, name, default_value=""):
        self.name = name
        self.default_value = default_value

    def capture(self, request):
        self.value = request.form.get(self.name, self.default_value)

class InputDropdown(BaseInput):
    def __init__(self, name, label, 
                 values, action_url="/", selected_value="Select All"):
        super().__init__(name, selected_value)
        
        self.label = label
        if isinstance(values, tuple) and len(values) == 2 and hasattr(values[0], 'loc'):
            self.values = ["Select All"] + values[0][values[1]].unique().tolist()
        elif isinstance(values, list):
            self.values = ["Select All"] + values
        else:
            raise ValueError("""Invalid values provided. It should be either 
                             a list or a tuple with DataFrame and column name.""")
        
        self.action_url = action_url
        self.selected_value = selected_value

    def capture(self, request):
        self.value = request.form.get(self.name)

        print(f"Captured value for {self.name}: {self.value}")  # debugging
        
        if not self.value:
            self.value = "Select All"
        self.selected_value = self.value

    def render(self):
        print("....Rendering dropdown....") 
        template = '''
        <div class="overflow-hidden">
            <label for="{{ name }}" 
                class="block text-sm font-medium text-red-700 mb-2">{{ label }}</label>
            <div class="relative">
                <select name="{{ name }}" 
                    class="w-full bg-white border border-gray-300 rounded-md py-2 px-4 
                    block w-full text-sm focus:outline-none focus:ring 
                    focus:ring-opacity-50 focus:ring-blue-500">
                        {% for value in values %}
                            <option value="{{ value }}" 
                                {% if value == selected_value %} 
                                    selected {% endif %} > {{ value }}
                            </option>
                        {% endfor %}
                </select>
            </div>
        </div>
        '''
        return render_template_string(
            template, name=self.name, label=self.label, 
            values=self.values, selected_value=self.selected_value)
class TextInput(BaseInput):
    def __init__(self, name, label, default_value=""):
        super().__init__(name, default_value)
        self.label = label

    def capture(self, request):
        self.value = request.form.get(self.name, self.default_value)
        self.default_value = self.value

    def render(self):
        template = '''
        <div class="overflow-hidden mb-4">
            <label for="{{ name }}" class="block text-sm font-medium 
            text-gray-700 mb-2">
                {{ label }}
            </label>
            <input 
                type="text" 
                id="{{ name }}" 
                name="{{ name }}" 
                value="{{ default_value }}" 
                class="w-full border border-gray-300 p-2 rounded-md 
                focus:outline-none focus:ring focus:ring-opacity-50 focus:ring-blue-500"
            >
        </div>
        '''
        return render_template_string(
            template, 
            name=self.name, 
            label=self.label, 
            default_value=self.default_value)

class InputSlider_Numerical(BaseInput):
    def __init__(self, name, label, min_value=0, 
                 max_value=100, step=1, default_value=50):
        
        # Initialize the base attributes
        super().__init__(name, default_value)

        self.label = label
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

    def capture(self, request):
        self.value = int(request.form.get(self.name, self.default_value))
        self.default_value = self.value

    def render(self):
        template = '''
        <div class="overflow-hidden mb-4">
            <label 
                for="{{ name }}" 
                class="block text-sm font-medium text-gray-700 mb-2"
            >
                {{ label }}
            </label>
            <input 
                type="range" 
                id="{{ name }}" 
                name="{{ name }}" 
                min="{{ min_value }}" 
                max="{{ max_value }}" 
                step="{{ step }}" 
                value="{{ default_value }}" 
                class="w-full border border-gray-300 p-2 rounded-md focus:outline-none 
                focus:ring focus:ring-opacity-50 focus:ring-blue-500" 
                oninput="updateOutput(this)"
            >
            <output 
                for="{{ name }}" 
                id="{{ name }}_output" 
                class="text-sm text-gray-500"
            >
                {{ default_value }}
            </output>
        </div>
        <script>
            function updateOutput(slider) {
                const output = document.getElementById(slider.id + "_output");
                output.value = slider.value;
            }
        </script>
        '''
        return render_template_string(
            template, name=self.name, label=self.label, 
            min_value=self.min_value, max_value=self.max_value, 
            step=self.step, default_value=self.default_value)

class InputSlider_Categorical(BaseInput):
    def __init__(self, name, label, categories, default_value=None):
        # Ensure the "Select All" is the first option only
        self.categories = ["Select All"] + [cat for cat in categories 
                                            if cat != "Select All"]
        
        # The default value would be the first category if not provided
        super().__init__(name, default_value if default_value else self.categories[0])
        
        self.label = label

    def capture(self, request):
        self.value = request.form.get(self.name, self.default_value)
        # Update the default_value to the captured value for rendering purposes
        self.default_value = self.value

    def render(self):
        template = '''
        <div class="overflow-hidden mb-4">
            <label 
                for="{{ name }}" 
                class="block text-sm font-medium text-gray-700 mb-2"
            >
                {{ label }}
            </label>
            <input 
                type="range" 
                id="{{ name }}_range" 
                min="0" 
                max="{{ max_position }}" 
                value="{{ default_position }}" 
                class="w-full border border-gray-300 p-2 
                rounded-md focus:outline-none focus:ring 
                focus:ring-opacity-50 focus:ring-blue-500"
                oninput="updateCategoryDisplay(this)"
            >
            <output 
                for="{{ name }}_range" 
                id="{{ name }}_output" 
                class="text-sm text-gray-500"
            >
                {{ categories[default_position] }}
            </output>
            <!-- Hidden field to store the category name -->
            <input 
                type="hidden" 
                id="{{ name }}" 
                name="{{ name }}" 
                value="{{ default_value }}"
            >
        </div>

        <script>
            function updateCategoryDisplay(slider) {
                const baseId = slider.id.replace("_range", "");
                const outputElement = document.getElementById(baseId + '_output');
                const hiddenInputElement = document.getElementById(baseId);
                const categories = {{ categories|tojson }};
                outputElement.textContent = categories[slider.value];
                hiddenInputElement.value = categories[slider.value]; 
            }
        </script>
        
        '''
        # Position is zero-indexed based on categories list
        default_position = self.categories.index(self.default_value)
        return render_template_string(template, name=self.name, label=self.label, 
                                      max_position=len(self.categories)-1, 
                                      default_position=default_position, 
                                      categories=self.categories)


class InputRadio(BaseInput):
    def __init__(self, name, label, options, default_value=None):
        # Ensure 'Select All' is the first option in the list
        if "Select All" not in options:
            options.insert(0, "Select All")

        # If no default_value is provided, set it to the first option
        super().__init__(name, default_value if default_value else options[0])

        self.label = label
        self.options = options

    def capture(self, request):
        captured_value = request.form.get(self.name)
        if not captured_value:
            # If no value is captured (i.e., no radio button was clicked),
            # keep the default_value unchanged.
            self.value = self.default_value
        else:
            self.value = captured_value
            # Update the default_value to the captured value for rendering purposes
            self.default_value = captured_value

    def render(self):
        template = '''
        <div class="overflow-hidden mb-4">
            <span 
                class="block text-sm font-medium text-gray-700 mb-2"
            >
                {{ label }}
            </span>
            {% for option in options %}
            <div class="flex items-center mb-2">
                <input 
                    type="radio" 
                    id="{{ name }}_{{ option }}" 
                    name="{{ name }}" 
                    value="{{ option }}" 
                    class="focus:ring-indigo-500 h-4 w-4 
                    text-indigo-600 border-gray-300"
                    {% if option == default_value %} checked {% endif %}
                >
                <label 
                    for="{{ name }}_{{ option }}" 
                    class="ml-3 block text-sm font-medium text-gray-900"
                >
                    {{ option }}
                </label>
            </div>
            {% endfor %}
        </div>
        '''
        return render_template_string(template, name=self.name, 
                                      label=self.label, options=self.options, 
                                      default_value=self.default_value)
