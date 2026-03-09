PRおよびビュー
===============

レビューの目的は、提案された変更が長期的に有用かつ維持可能であることを保証することです。投稿者は以下の基準を考慮し、査読者は評価すべきです。

PR ディスクリプション
---------------

- 意味のあるタイトルを付けます：変更履歴を作成したり、古いPRを検索する際に扱い易いです。
- なぜPRを統合すべきかについて、動機付けを行ってください:コードの追加や変更は新たなバグを引き起こすリスクがあります。 個人的には、1人の方が「あれば嬉しい機能」を要望されるだけでは、条件に満たないと考えます。
- PRがディスクリプションにおいて、何をするのか説明してください:それによって、レビューの作成が、より簡単かつ迅速になります。
- PRはできるだけ小規模なものにしてください： 1つのPRで1000行をレビューするよりも、5本(PRs200ライン)をレビューする方が、はるかに簡単です。
- 他の進行中のPRと競合することがわかっている場合、調整を試み、相互に関連付けを行います。
　- 適宜、所望の審査/統合の順序を説明してください
- 複数のPRが必要な複雑な変更については 、何が完了し、何が残っているかを管理するためのイシューを作成します。
- PRは  単一のバグ修正や機能に焦点を当てているのでしょうか?
  - 独立した変更を、別々のPRに移すことを検討してください。

パブリックインターフェイス
-----------------

- 包括的なテストはありますか？
- インターフェースは、使用事例に合っていますか、また使用事例についての説明はありますか？
  - 直感による使用ですか？
  - 本当にこれをパブリックインターフェースとして所望し、維持していますか?
- is the interface API consistent with existing ones?
  - e.g. if everything else takes execution space instances as the first argument, don't make it the last argument
  - does the naming style match other Kokkos APIs
- are the interface semantics consistent with existing ones?
  - if everything else (or at least the majority) of interfaces taking an execution space instance argument is async, then new interfaces taking one should be too
- For any routine that's going to launch any parallel work, does it have an overload that takes an execution space instance, and does that overload use the instance for all parallel work?
- if the functionality is similar to an ISO C++ functionality, is the interface and behavior similar, and in places where it's not is it a conscious decision
- is there a corresponding API documentation PR
- Are the corner cases handled (works correctly, won't compile, detected at run time)?
- Do the C++ defaulted functions do the right thing (including if needed to be marked with KOKKOS_DEFAULTED_FUNCTION)?


Internal Implementation
-----------------------

- is the implementation style consistent with the rest of Kokkos
- is there unnecessary code duplication
  - in particular: is code that can be shared across backends shared?
- did it go in the right sub-part of Kokkos (core, algorithms, containers etc.)
- are there debug checks we should add?
  - like do the arguments make sense together etc.
- are implementation details accidentally exposed?
- is there unnecessary fencing
- are there unnecessary allocations/deallocations
- Avoiding tangle of inclusions: are headers/files including only what is needed?
- Is the code expressing intent clearly (choosing expressive names for variables, functions, etc)?
- Are changes in the code and intent properly captured in the description of the PR?
- consider appropriateness of tests for implementation details
  - we want to avoid needing to touch many tests for changes in on internal details

Tests
---------------

- For bug fix PRs: add test which would catch the issue without the fix
- Do newly added tests have the correct granularity?
- Do tests have a suitable runtime or are unnecessarily large?

Reviewer Behavior
-----------------

- provide timely feedback and respond to changes by the author of the pull request in a reasonable amount of time; it's best to give feedback to pull requests as quickly as possible.
- only request changes if they are ready to resolve the request upon changes by the author of the pull request; stalling pull requests for requested changes that have been addressed is a problem.
- only review pull requests that have been marked as ready; we have a bunch of pull requests that explore the feasibility of ideas and just need the CI to run. Similarly, pull requests should only be marked as "ready for review" if the author is reasonably happy with the status. If the author mostly seeks feedback on general design and direction, this should be clearly communicated in the pull request description (either "draft" or "ready for review").
- mirror communication with pull request author outside of pull requests (on slack, in person, video calls, etc.) in comments to the pull request.
- contact authors directly if more clarification is needed.
- not be afraid of reviewing pull requests even if they are (slightly) outside their comfort zone.
- work with authors to bring issues/questions that need a quorum/discussion with a larger audience to the developer meeting.
