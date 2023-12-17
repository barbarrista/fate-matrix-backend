from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from app.core.domain.fate_matrix.dto import PointBundleDTO
from app.core.template_builder.enums import TemplatePath
from app.settings import BASE_DIR


class TemplateBuilder:
    templates_dir = "templates"

    def __init__(self) -> None:
        full_path = Path(BASE_DIR, Path(Path(__file__).parent, self.templates_dir))
        template_loader = FileSystemLoader(full_path.as_posix())
        self._enviroment = Environment(loader=template_loader, autoescape=True)

    def personal_fate_matrix(self, dto: PointBundleDTO) -> str:
        template = TemplatePath.personal_fate_matrix
        jinja_template = self._enviroment.get_template(template.value)
        return jinja_template.render(dto=dto)
