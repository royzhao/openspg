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


class ConceptLayerConfig(object):
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
        'hypernym_predicate': 'str',
        'layer_names': 'list[str]'
    }

    attribute_map = {
        'hypernym_predicate': 'hypernymPredicate',
        'layer_names': 'layerNames'
    }

    def __init__(self, hypernym_predicate=None, layer_names=None, local_vars_configuration=None):  # noqa: E501
        """ConceptLayerConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hypernym_predicate = None
        self._layer_names = None
        self.discriminator = None

        if hypernym_predicate is not None:
            self.hypernym_predicate = hypernym_predicate
        if layer_names is not None:
            self.layer_names = layer_names

    @property
    def hypernym_predicate(self):
        """Gets the hypernym_predicate of this ConceptLayerConfig.  # noqa: E501


        :return: The hypernym_predicate of this ConceptLayerConfig.  # noqa: E501
        :rtype: str
        """
        return self._hypernym_predicate

    @hypernym_predicate.setter
    def hypernym_predicate(self, hypernym_predicate):
        """Sets the hypernym_predicate of this ConceptLayerConfig.


        :param hypernym_predicate: The hypernym_predicate of this ConceptLayerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = [None, "isA", "locateAt"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and hypernym_predicate not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `hypernym_predicate` ({0}), must be one of {1}"  # noqa: E501
                .format(hypernym_predicate, allowed_values)
            )

        self._hypernym_predicate = hypernym_predicate

    @property
    def layer_names(self):
        """Gets the layer_names of this ConceptLayerConfig.  # noqa: E501


        :return: The layer_names of this ConceptLayerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._layer_names

    @layer_names.setter
    def layer_names(self, layer_names):
        """Sets the layer_names of this ConceptLayerConfig.


        :param layer_names: The layer_names of this ConceptLayerConfig.  # noqa: E501
        :type: list[str]
        """

        self._layer_names = layer_names

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
        if not isinstance(other, ConceptLayerConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConceptLayerConfig):
            return True

        return self.to_dict() != other.to_dict()
