# coding: utf-8

"""
Copyright 2015 SmartBear Software

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


class NodesLnnStatusNodeCpu(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodesLnnStatusNodeCpu - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'model': 'str',
            'overtemp': 'str',
            'proc': 'str',
            'speed_limit': 'str'
        }

        self.attribute_map = {
            'model': 'model',
            'overtemp': 'overtemp',
            'proc': 'proc',
            'speed_limit': 'speed_limit'
        }

        self._model = None
        self._overtemp = None
        self._proc = None
        self._speed_limit = None

    @property
    def model(self):
        """
        Gets the model of this NodesLnnStatusNodeCpu.
        Manufacturer model description of this CPU.

        :return: The model of this NodesLnnStatusNodeCpu.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this NodesLnnStatusNodeCpu.
        Manufacturer model description of this CPU.

        :param model: The model of this NodesLnnStatusNodeCpu.
        :type: str
        """
        self._model = model

    @property
    def overtemp(self):
        """
        Gets the overtemp of this NodesLnnStatusNodeCpu.
        CPU overtemp state.

        :return: The overtemp of this NodesLnnStatusNodeCpu.
        :rtype: str
        """
        return self._overtemp

    @overtemp.setter
    def overtemp(self, overtemp):
        """
        Sets the overtemp of this NodesLnnStatusNodeCpu.
        CPU overtemp state.

        :param overtemp: The overtemp of this NodesLnnStatusNodeCpu.
        :type: str
        """
        self._overtemp = overtemp

    @property
    def proc(self):
        """
        Gets the proc of this NodesLnnStatusNodeCpu.
        Type of processor and core of this CPU.

        :return: The proc of this NodesLnnStatusNodeCpu.
        :rtype: str
        """
        return self._proc

    @proc.setter
    def proc(self, proc):
        """
        Sets the proc of this NodesLnnStatusNodeCpu.
        Type of processor and core of this CPU.

        :param proc: The proc of this NodesLnnStatusNodeCpu.
        :type: str
        """
        self._proc = proc

    @property
    def speed_limit(self):
        """
        Gets the speed_limit of this NodesLnnStatusNodeCpu.
        CPU throttling (expressed as a percentage).

        :return: The speed_limit of this NodesLnnStatusNodeCpu.
        :rtype: str
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """
        Sets the speed_limit of this NodesLnnStatusNodeCpu.
        CPU throttling (expressed as a percentage).

        :param speed_limit: The speed_limit of this NodesLnnStatusNodeCpu.
        :type: str
        """
        self._speed_limit = speed_limit

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

