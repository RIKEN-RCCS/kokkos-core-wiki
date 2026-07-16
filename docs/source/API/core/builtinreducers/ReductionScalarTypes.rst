縮約スカラー型
##############

対応する組み込みリデューサーを使用しながら、``parallel_reduce()`` の結果を保持するために設計された型です。

.. list-table::
   :widths: 20 65 15
   :header-rows: 1

   * - クラステンプレート
     - 説明
     - 組み込みリデューサー
   * - :doc:`FirstLocScalar`
     - 条件を満たす最初の位置を格納します。
     - :cpp:class:`FirstLoc`
   * - :doc:`LastLocScalar`
     - 条件を満たす最後の位置を格納します。
     - :cpp:class:`LastLoc`
   * - :doc:`MinMaxLocScalar`
     - 最小値、最大値、およびそれぞれの保存先を格納します。
     - :cpp:class:`MinMaxLoc`
   * - :doc:`MinMaxScalar`
     - 最小値と最大値を格納します。
     - :cpp:class:`MinMax`
   * - :doc:`ValLocScalar`
     - 単一の値とその位置を格納します。
     - :cpp:class:`MinLoc`, :cpp:class:`MaxLoc`

.. toctree::
   :hidden:
   :maxdepth: 1

   FirstLocScalar
   LastLocScalar
   MinMaxLocScalar
   MinMaxScalar
   ValLocScalar
