from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class test_600(ComponentSpec):
    name: str = "test_600"
    category: str = "Custom"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class test_600Properties(ComponentProperties):
        # properties for the component with default values
        my_property: SString = SString("default value of my property")

    def dialog(self) -> Dialog:
        # Define the UI dialog structure for the component
        return Dialog("test_600")

    def validate(self, context: WorkflowContext, component: Component[test_600Properties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def onChange(self, context: WorkflowContext, oldState: Component[test_600Properties], newState: Component[test_600Properties]) -> Component[
    test_600Properties]:
        # Handle changes in the component's state and return the new state
        return newState


    class test_600Code(ComponentCode):
        def __init__(self, newProps):
            self.props: test_600.test_600Properties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            # This method contains logic used to generate the spark code from the given inputs.
            return in0
