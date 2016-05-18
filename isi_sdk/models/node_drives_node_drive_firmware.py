# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class NodeDrivesNodeDriveFirmware(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodeDrivesNodeDriveFirmware - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_firmware': 'str',
            'desired_firmware': 'str'
        }

        self.attribute_map = {
            'current_firmware': 'current_firmware',
            'desired_firmware': 'desired_firmware'
        }

        self._current_firmware = None
        self._desired_firmware = None

    @property
    def current_firmware(self):
        """
        Gets the current_firmware of this NodeDrivesNodeDriveFirmware.
        This drive's current firmware revision

        :return: The current_firmware of this NodeDrivesNodeDriveFirmware.
        :rtype: str
        """
        return self._current_firmware

    @current_firmware.setter
    def current_firmware(self, current_firmware):
        """
        Sets the current_firmware of this NodeDrivesNodeDriveFirmware.
        This drive's current firmware revision

        :param current_firmware: The current_firmware of this NodeDrivesNodeDriveFirmware.
        :type: str
        """
        
        self._current_firmware = current_firmware

    @property
    def desired_firmware(self):
        """
        Gets the desired_firmware of this NodeDrivesNodeDriveFirmware.
        This drive's desired firmware revision.

        :return: The desired_firmware of this NodeDrivesNodeDriveFirmware.
        :rtype: str
        """
        return self._desired_firmware

    @desired_firmware.setter
    def desired_firmware(self, desired_firmware):
        """
        Sets the desired_firmware of this NodeDrivesNodeDriveFirmware.
        This drive's desired firmware revision.

        :param desired_firmware: The desired_firmware of this NodeDrivesNodeDriveFirmware.
        :type: str
        """
        
        self._desired_firmware = desired_firmware

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
