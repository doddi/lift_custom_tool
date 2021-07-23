#!/usr/bin/env python3
from sonatypeliftlib.apiv1 import ApiV1, ToolNote

class CustomTool(ApiV1):
    def tool_applicable(self):
        return ApiV1.is_applicable()

    def tool_run(self):
        tool_notes = []

        tn1 = ToolNote("Foo", "Foo Message", None, None, None)
        tool_notes.append(tn1)

        tn2 = ToolNote("Bar", "Bar Message", None, 1, None)
        tool_notes.append(tn2)
        return tool_notes

def main():
    tool = CustomTool("MyCustomTool")
    tool.service()

if __name__ == "__main__":
    main()

