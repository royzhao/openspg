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


class PredicateIdentifier(object):
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
        'identity_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'identity_type': 'identityType',
        'name': 'name'
    }

    def __init__(self, identity_type='PREDICATE', name=None, local_vars_configuration=None):  # noqa: E501
        """PredicateIdentifier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._identity_type = None
        self._name = None
        self.discriminator = identity_type

        self.identity_type = identity_type
        if name is not None:
            self.name = name

    @property
    def identity_type(self):
        """Gets the identity_type of this PredicateIdentifier.  # noqa: E501


        :return: The identity_type of this PredicateIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """Sets the identity_type of this PredicateIdentifier.


        :param identity_type: The identity_type of this PredicateIdentifier.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and identity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `identity_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SPG_TYPE", "SPG_TRIPLE", "CONCEPT", "PREDICATE", "OPERATOR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and identity_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `identity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(identity_type, allowed_values)
            )

        self._identity_type = identity_type

    @property
    def name(self):
        """Gets the name of this PredicateIdentifier.  # noqa: E501


        :return: The name of this PredicateIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredicateIdentifier.


        :param name: The name of this PredicateIdentifier.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, PredicateIdentifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredicateIdentifier):
            return True

        return self.to_dict() != other.to_dict()
