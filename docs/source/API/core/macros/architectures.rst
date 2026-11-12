アーキテクチャ
==============

``KOKKOS_ARCH_*`` マクロは、Kokkos がターゲットとするように設定されたハードウェアアーキテクチャを記録します。

.. warning::

   コードを ``KOKKOS_ARCH_*`` マクロに依存させることは避けてください。Kokkos はアーキテクチャ固有の最適化を内部的に処理しており、これらのマクロはコードを特定のビルド設定に結びつけてしまいます。

CMake オプションとの関係
------------------------

Kokkos を ``-DKokkos_ARCH_<NAME>=ON`` で設定すると、マクロ ``KOKKOS_ARCH_<NAME>`` が定義されます。たとえば、``-DKokkos_ARCH_AMPERE80=ON`` は ``KOKKOS_ARCH_AMPERE80`` を定義します。

いくつかのアーキテクチャは異なるマクロ名を使用します。たとえば、Kokkos は設定時に AMD Zen のキーワード ``Kokkos_ARCH_ZEN``、``Kokkos_ARCH_ZEN2``、... ``Kokkos_ARCH_ZEN5`` を ``KOKKOS_ARCH_AMD_ZEN``、``KOKKOS_ARCH_AMD_ZEN2``、... ``KOKKOS_ARCH_AMD_ZEN5`` にマッピングします。

サポートされているアーキテクチャの完全な一覧は、:ref:`設定ガイドのアーキテクチャのセクション <keywords_arch>`\ にあります。不明な場合は、ビルド用に定義されたマクロについて、インストール時に生成される ``KokkosCore_config.h`` ヘッダーを確認してください。

CMake に対応するもののないマクロ
--------------------------------

``KOKKOS_ARCH_AMD_GPU``
   AMD GPU 向けのアーキテクチャフラグを保持する文字列として定義されます（MI250X アクセラレータをターゲットとする場合は ``"gfx90A"`` など）。