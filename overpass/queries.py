# -*- coding: utf-8 -*-


class MapQuery(object):

    """Query to retrieve complete ways and relations in an area."""

    _QUERY_TEMPLATE = "(node({south},{west},{north},{east});<;);"

    def __init__(self, south, west, north, east):
        """
        Initialize query with given bounding box.
        :param: bbox Bounding box with limit values in format west, south,
                east, north.
        """
        self.west = west
        self.south = south
        self.east = east
        self.north = north

    def __str__(self):
        return self._QUERY_TEMPLATE.format(west=self.west, south=self.south,
                                           east=self.east, north=self.north)


class NodeQuery(object):

    """Query to retrieve a set of nodes and their dependent nodes satisfying
       the input parameters"""

    _QUERY_TEMPLATE = "(node{query_parameters});(._;>;);"

    def __init__(self, query_parameters):
        """
        Initialize a query for a set of ways satisfying the given parameters.
        :param query_parameters: Overpass QL query parameters
        """
        self.query_parameters = query_parameters

    def __str__(self):
        return self._QUERY_TEMPLATE.format(query_parameters=self.query_parameters)


class WayQuery(object):

    """Query to retrieve a set of ways and their dependent nodes satisfying
       the input parameters"""

    _QUERY_TEMPLATE = "(way{query_parameters});(._;>;);"

    def __init__(self, query_parameters):
        """
        Initialize a query for a set of ways satisfying the given parameters.
        :param query_parameters: Overpass QL query parameters
        """
        self.query_parameters = query_parameters

    def __str__(self):
        return self._QUERY_TEMPLATE.format(query_parameters=self.query_parameters)


class RelQuery(object):

    """Query to retrieve a set of relation and their dependent ways and/or
       nodes satisfying the input parameters"""

    _QUERY_TEMPLATE = "(relation{query_parameters});(._;>;);"

    def __init__(self, query_parameters):
        """
        Initialize a query for a set of ways satisfying the given parameters.
        :param query_parameters: Overpass QL query parameters
        """
        self.query_parameters = query_parameters

    def __str__(self):
        return self._QUERY_TEMPLATE.format(query_parameters=self.query_parameters)
