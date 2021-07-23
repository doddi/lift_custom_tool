#!/usr/bin/env python3
import sys
from sonatypeliftlib.apiv1 import ApiV1, ToolNote

class CustomTool(ApiV1):
    def tool_applicable(self):
        return ApiV1.is_applicable()

    def tool_run(self):
        tool_notes = []

        tn1 = ToolNote("Foo", "Foo Message", "foo.txt", None, None)
        tool_notes.append(tn1)

        tn2 = ToolNote("Bar", "Bar Message", "bar.yml", 1, None)
        tool_notes.append(tn2)
        return tool_notes

def main():
    tool = CustomTool("MyCustomTool", sys.argv)
    tool.service()

if __name__ == "__main__":
    main()

