import markdown
import os
from typing import Optional


def _create_diagram(zip_code: Optional[str] = None, aggregated: Optional[bool] = None,
                    data_ex: Optional[str] = None, path: str = 'diagram.html') -> None:
    """
    Function to create an HTML diagram depicting the interaction between User, System, and OpenWeather API.

    Args:
        zip_code (str, optional): User's zip code. Defaults to None.
        aggregated (bool, optional): Determines whether the weather data should be aggregated. Defaults to None.
        data_ex (str, optional): Example of output data. Defaults to None.
        path (str, optional): Path where the HTML file will be stored. Defaults to 'diagram.html'.

    Returns:
        None
    """
    new_line = '\n'
    diagram_definition = f"""
# Weather Weekend API

Execution graph for weekend weather API

~~~mermaid
sequenceDiagram
        participant U as User
        participant S as System
        participant O as OpenWeather API
        U->>S: ZIP {str(zip_code) if zip_code else ''} | aggregated {str(aggregated) if aggregated is None else ''} 
        S->>O: Request weather data
        O-->>S: Return weather data
        S->>S: Clean API response
        S-->>U: Display weather prediction
~~~

{'##Output Example:' + new_line + data_ex if data_ex else ''}
_____

"""

    # Fix compatibility bug
    html = markdown.markdown(diagram_definition, extensions=['md_mermaid']).replace("<script>",
                                                                                    '<script src="mermaid.min.js">')

    # Create folders if they don't exist
    os.makedirs(path, exist_ok=True)

    # Write the generated HTML to a file
    with open(os.path.join(path, 'diagram.html'), 'w') as f:
        f.write(html)
