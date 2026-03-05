``MinMaxScalar``
================

.. role::cpp(code)
    :language: cpp

:cpp:struct:`MinMaxScalar` は、
単一の便利な単位として、最小値および最大値は、クラステンプレートです。主に、:cpp:class:`MinMax` builtin リデューサーを使って :cpp:func:`parallel_reduce` 演算の結果保持を目的として設計されています。


It is generally recommended to get this type by using the reducer's
``::value_type`` member (e.g., ``MinMax<Scalar,Space>::value_type``) to ensure
the correct template parameters are used.

Header File: ``<Kokkos_Core.hpp>``

Usage
-----

.. code-block:: cpp

   MinMax<T,S>::value_type result;
   parallel_reduce(N,Functor,MinMax<T,S>(result));
   T minValue = result.min_val;
   T maxValue = result.max_val;

Interface
---------

.. cpp:struct::  template<class Scalar> MinMaxScalar

   :tparam Scalar: The data type of the value being reduced (e.g., ``double``, ``int``).

   .. rubric:: Data members

   .. cpp:var:: Scalar min_val

      The reduced minimum value.

   .. cpp:var:: Scalar max_val

      The reduced maximum value.
