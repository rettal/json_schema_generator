# -*- coding: utf-8 -*-

import types


class Type(object):

    schema_version = u"http://json-schema.org/draft-03/schema"
    json_type = None
    id = None
    required = False

    @classmethod
    def get_schema_type_for(self, t):
        """docstring for get_schema_type_for"""

        schema_type = SCHEMA_TYPES.get(t)

        if not schema_type:
            raise JsonSchemaTypeNotFound(
                "There is no schema type for %s.\n Try:\n %s" % (
                    str(t), ",\n".join(["\t%s" % str(k) for k in SCHEMA_TYPES.keys()])
                )
            )

        return schema_type


class IntegerType(object):
    json_type = "number"


class StringType(object):
    json_type = "string"


class NullType(object):
    json_type = "null"


class BooleanType(object):
    json_type = "boolean"


class ArrayType(object):
    json_type = "array"
    items = []


class ObjectType(object):
    json_type = "object"
    properties = {}


class JsonSchemaTypeNotFound(Exception):
    pass


SCHEMA_TYPES = {
    types.NoneType: NullType,
    types.UnicodeType: StringType,
    types.StringType: StringType,
    types.IntType: IntegerType,
    types.FloatType: IntegerType,
    types.BooleanType: BooleanType,
    types.ListType: ArrayType,
    types.DictType: ObjectType,
}
