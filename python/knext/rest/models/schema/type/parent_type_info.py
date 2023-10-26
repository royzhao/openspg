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


class ParentTypeInfo(object):
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
        'unique_id': 'int',
        'parent_unique_id': 'int',
        'parent_type_identifier': 'SpgTypeIdentifier',
        'inherit_path': 'list[int]'
    }

    attribute_map = {
        'unique_id': 'uniqueId',
        'parent_unique_id': 'parentUniqueId',
        'parent_type_identifier': 'parentTypeIdentifier',
        'inherit_path': 'inheritPath'
    }

    def __init__(self, unique_id=None, parent_unique_id=None, parent_type_identifier=None, inherit_path=None,
                 local_vars_configuration=None):  # noqa: E501
        """ParentTypeInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._unique_id = None
        self._parent_unique_id = None
        self._parent_type_identifier = None
        self._inherit_path = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if parent_unique_id is not None:
            self.parent_unique_id = parent_unique_id
        if parent_type_identifier is not None:
            self.parent_type_identifier = parent_type_identifier
        if inherit_path is not None:
            self.inherit_path = inherit_path

    @property
    def unique_id(self):
        """Gets the unique_id of this ParentTypeInfo.  # noqa: E501


        :return: The unique_id of this ParentTypeInfo.  # noqa: E501
        :rtype: int
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this ParentTypeInfo.


        :param unique_id: The unique_id of this ParentTypeInfo.  # noqa: E501
        :type: int
        """

        self._unique_id = unique_id

    @property
    def parent_unique_id(self):
        """Gets the parent_unique_id of this ParentTypeInfo.  # noqa: E501


        :return: The parent_unique_id of this ParentTypeInfo.  # noqa: E501
        :rtype: int
        """
        return self._parent_unique_id

    @parent_unique_id.setter
    def parent_unique_id(self, parent_unique_id):
        """Sets the parent_unique_id of this ParentTypeInfo.


        :param parent_unique_id: The parent_unique_id of this ParentTypeInfo.  # noqa: E501
        :type: int
        """

        self._parent_unique_id = parent_unique_id

    @property
    def parent_type_identifier(self):
        """Gets the parent_type_identifier of this ParentTypeInfo.  # noqa: E501


        :return: The parent_type_identifier of this ParentTypeInfo.  # noqa: E501
        :rtype: SpgTypeIdentifier
        """
        return self._parent_type_identifier

    @parent_type_identifier.setter
    def parent_type_identifier(self, parent_type_identifier):
        """Sets the parent_type_identifier of this ParentTypeInfo.


        :param parent_type_identifier: The parent_type_identifier of this ParentTypeInfo.  # noqa: E501
        :type: SpgTypeIdentifier
        """

        self._parent_type_identifier = parent_type_identifier

    @property
    def inherit_path(self):
        """Gets the inherit_path of this ParentTypeInfo.  # noqa: E501


        :return: The inherit_path of this ParentTypeInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._inherit_path

    @inherit_path.setter
    def inherit_path(self, inherit_path):
        """Sets the inherit_path of this ParentTypeInfo.


        :param inherit_path: The inherit_path of this ParentTypeInfo.  # noqa: E501
        :type: list[int]
        """

        self._inherit_path = inherit_path

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
        if not isinstance(other, ParentTypeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParentTypeInfo):
            return True

        return self.to_dict() != other.to_dict()
