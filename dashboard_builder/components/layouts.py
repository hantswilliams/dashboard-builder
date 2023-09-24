class ColumnLayout:
    def __init__(self, num_columns):
        """Initializes a layout with the specified columns.

        Args:
        - *num_columns (int): Number of columns to be created.
        """
        self.columns = [[] for _ in range(num_columns)]

    def add_to_column(self, col_index, *components):
        """Add components to a specific column.

        Args:
        - col_index (int): The index of the column to add to.
        - *components: Components to add to the column.
        """
        for component in components:
            self.columns[col_index].append(component)

    def render(self):
        rendered_columns = []
        for column in self.columns:
            rendered_components = [comp.render() for comp in column]
            rendered_columns.append(
                f"<div class='flex-grow w-full md:flex-grow-0 md:w-1/2 px-2 max-h-[75vh] max-w-[90%] overflow-y-auto'>{'' .join(rendered_components)}</div>")  # noqa: E501
        return f"<div class='flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-2'>{'' .join(rendered_columns)}</div>"  # noqa: E501


