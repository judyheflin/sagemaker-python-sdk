# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""The step definitions for workflow."""
from __future__ import absolute_import

from typing import List, Union

from sagemaker.workflow import PipelineNonPrimitiveInputTypes
from sagemaker.workflow.entities import (
    RequestType,
)
from sagemaker.workflow.steps import Step, StepTypeEnum


class FailStep(Step):
    """Fail step for workflow."""

    def __init__(
        self,
        name: str,
        error_message: Union[str, PipelineNonPrimitiveInputTypes] = None,
        display_name: str = None,
        description: str = None,
        depends_on: Union[List[str], List[Step]] = None,
    ):
        """Constructs a FailStep.

        Args:
            name (str): The name of the fail step. A name is required and must be unique within an account.
            error_message (str or PipelineNonPrimitiveInputTypes): An error message defined by the user.
                Once the fail step is reached, the execution will fail and the
                error message will be set as the failure reason (default: None).
            display_name (str): The display name of the fail step. The display name provides better readability 
                for fail step naming conventions that are auto-generated with random numbers or timestamps. (default: None).
            description (str): The description of the fail step (default: None).
            depends_on (List[str] or List[Step]): A list of step names or step instances
                that this fail step depends on (default: None).
        """
        super(FailStep, self).__init__(
            name, display_name, description, StepTypeEnum.FAIL, depends_on
        )
        self.error_message = error_message if error_message is not None else ""

    @property
    def arguments(self) -> RequestType:
        """The arguments dict that is used to define the Fail step."""
        return dict(ErrorMessage=self.error_message)

    @property
    def properties(self):
        """A Properties object is not available for the Fail step"""
        raise RuntimeError(
            "The Properties object is not available for the Fail step "
            + "as it cannot be referenced by other steps."
        )
