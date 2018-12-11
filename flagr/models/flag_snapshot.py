# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flagr.models.flag import Flag  # noqa: F401,E501


class FlagSnapshot(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'updated_by': 'str',
        'flag': 'Flag',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'updated_by': 'updatedBy',
        'flag': 'flag',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, updated_by=None, flag=None, updated_at=None):  # noqa: E501
        """FlagSnapshot - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._updated_by = None
        self._flag = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        if updated_by is not None:
            self.updated_by = updated_by
        self.flag = flag
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this FlagSnapshot.  # noqa: E501


        :return: The id of this FlagSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlagSnapshot.


        :param id: The id of this FlagSnapshot.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def updated_by(self):
        """Gets the updated_by of this FlagSnapshot.  # noqa: E501


        :return: The updated_by of this FlagSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this FlagSnapshot.


        :param updated_by: The updated_by of this FlagSnapshot.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def flag(self):
        """Gets the flag of this FlagSnapshot.  # noqa: E501


        :return: The flag of this FlagSnapshot.  # noqa: E501
        :rtype: Flag
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this FlagSnapshot.


        :param flag: The flag of this FlagSnapshot.  # noqa: E501
        :type: Flag
        """
        if flag is None:
            raise ValueError("Invalid value for `flag`, must not be `None`")  # noqa: E501

        self._flag = flag

    @property
    def updated_at(self):
        """Gets the updated_at of this FlagSnapshot.  # noqa: E501


        :return: The updated_at of this FlagSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FlagSnapshot.


        :param updated_at: The updated_at of this FlagSnapshot.  # noqa: E501
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501
        if updated_at is not None and len(updated_at) < 1:
            raise ValueError("Invalid value for `updated_at`, length must be greater than or equal to `1`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, FlagSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
