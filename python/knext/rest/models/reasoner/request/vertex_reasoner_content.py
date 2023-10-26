# coding: utf-8

"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

#  Copyright 2023 Ant Group CO., Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
#  in compliance with the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under the License
#  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied.

import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class VertexReasonerContent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'starting_vertices': 'list[StartingVertex]',
        'param_type': 'str'
    }

    attribute_map = {
        'starting_vertices': 'startingVertices',
        'param_type': 'paramType'
    }

    def __init__(self, starting_vertices=None, param_type='VERTEX', local_vars_configuration=None):  # noqa: E501
        """VertexReasonerContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._starting_vertices = None
        self._param_type = None
        self.discriminator = param_type

        self.starting_vertices = starting_vertices
        self.param_type = param_type

    @property
    def starting_vertices(self):
        """Gets the starting_vertices of this VertexReasonerContent.  # noqa: E501


        :return: The starting_vertices of this VertexReasonerContent.  # noqa: E501
        :rtype: list[StartingVertex]
        """
        return self._starting_vertices

    @starting_vertices.setter
    def starting_vertices(self, starting_vertices):
        """Sets the starting_vertices of this VertexReasonerContent.


        :param starting_vertices: The starting_vertices of this VertexReasonerContent.  # noqa: E501
        :type: list[StartingVertex]
        """
        if self.local_vars_configuration.client_side_validation and starting_vertices is None:  # noqa: E501
            raise ValueError("Invalid value for `starting_vertices`, must not be `None`")  # noqa: E501

        self._starting_vertices = starting_vertices

    @property
    def param_type(self):
        """Gets the param_type of this VertexReasonerContent.  # noqa: E501


        :return: The param_type of this VertexReasonerContent.  # noqa: E501
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this VertexReasonerContent.


        :param param_type: The param_type of this VertexReasonerContent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and param_type is None:  # noqa: E501
            raise ValueError("Invalid value for `param_type`, must not be `None`")  # noqa: E501
        allowed_values = ["VERTEX", "KGDSL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and param_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `param_type` ({0}), must be one of {1}"  # noqa: E501
                .format(param_type, allowed_values)
            )

        self._param_type = param_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VertexReasonerContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VertexReasonerContent):
            return True

        return self.to_dict() != other.to_dict()
