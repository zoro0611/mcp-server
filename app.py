from fastmcp import FastMCP

app = FastMCP("My FastMCP Server")
#提供一個加法的工具

@app.tool
def add(n1:int, n2:int) -> int:
    """加法工具"""
    return n1 + n2