from unittest import IsolatedAsyncioTestCase

from responses.registries import OrderedRegistry
from responses_server import ResponsesServer

from videosrc.crawl.peertube import PeerTubeCrawler


RSP0 = {'avatars': [],
 'banners': [],
 'createdAt': '2022-07-31T00:50:59.621Z',
 'description': None,
 'displayName': "Ben's channel",
 'followersCount': 0,
 'followingCount': 0,
 'host': 'cesium.tv:80',
 'hostRedundancyAllowed': False,
 'id': 2,
 'isLocal': True,
 'name': 'btimby_channel',
 'ownerAccount': {'avatars': [],
                  'banners': [],
                  'createdAt': '2022-07-31T00:50:59.616Z',
                  'description': None,
                  'displayName': 'btimby',
                  'followersCount': 0,
                  'followingCount': 0,
                  'host': 'cesium.tv:80',
                  'hostRedundancyAllowed': False,
                  'id': 3,
                  'name': 'btimby',
                  'updatedAt': '2022-07-31T00:50:59.619Z',
                  'url': 'http://cesium.tv/accounts/btimby',
                  'userId': 2},
 'support': None,
 'updatedAt': '2022-07-31T01:01:58.517Z',
 'url': 'http://cesium.tv/video-channels/btimby_channel'}
RSP1 = {'data': [{'account': {'avatars': [],
                       'displayName': 'btimby',
                       'host': 'cesium.tv:80',
                       'id': 3,
                       'name': 'btimby',
                       'url': 'http://cesium.tv/accounts/btimby'},
           'category': {'id': None, 'label': 'Misc'},
           'channel': {'avatars': [],
                       'displayName': "Ben's channel",
                       'host': 'cesium.tv:80',
                       'id': 2,
                       'name': 'btimby_channel',
                       'url': 'http://cesium.tv/video-channels/btimby_channel'},
           'createdAt': '2022-07-31T00:55:09.068Z',
           'description': 'The first Blender Open Movie from 2006',
           'dislikes': 0,
           'duration': 654,
           'embedPath': '/videos/embed/90222ccf-0d6d-43b4-ac4b-29f5da46119c',
           'id': 2,
           'isLive': False,
           'isLocal': True,
           'language': {'id': None, 'label': 'Unknown'},
           'licence': {'id': None, 'label': 'Unknown'},
           'likes': 0,
           'name': 'ElephantsDream',
           'nsfw': False,
           'originallyPublishedAt': None,
           'previewPath': '/lazy-static/previews/e783f6af-5a7d-437f-b019-522b5b9af5bb.jpg',
           'privacy': {'id': 1, 'label': 'Public'},
           'publishedAt': '2022-07-31T00:59:06.665Z',
           'shortUUID': 'iNid2sMo2cZQrJBnipxiXs',
           'thumbnailPath': '/static/thumbnails/cdb1f979-c288-454a-851e-f3b7b72a586f.jpg',
           'updatedAt': '2022-07-31T00:59:06.665Z',
           'url': 'http://cesium.tv/videos/watch/90222ccf-0d6d-43b4-ac4b-29f5da46119c',
           'uuid': '90222ccf-0d6d-43b4-ac4b-29f5da46119c',
           'viewers': 0,
           'views': 0},
          {'account': {'avatars': [],
                       'displayName': 'btimby',
                       'host': 'cesium.tv:80',
                       'id': 3,
                       'name': 'btimby',
                       'url': 'http://cesium.tv/accounts/btimby'},
           'category': {'id': 4, 'label': 'Art'},
           'channel': {'avatars': [],
                       'displayName': "Ben's channel",
                       'host': 'cesium.tv:80',
                       'id': 2,
                       'name': 'btimby_channel',
                       'url': 'http://cesium.tv/video-channels/btimby_channel'},
           'createdAt': '2022-07-31T00:52:47.770Z',
           'description': 'Big Buck Bunny tells the story of a giant rabbit '
                          'with a heart bigger than himself. When one sunny '
                          'day three rodents rudely harass him, something '
                          "snaps... and the rabbit ain't no bunny anymore! In "
                          'the typical cartoon tradition he prepares the '
                          'nasty...',
           'dislikes': 0,
           'duration': 596,
           'embedPath': '/videos/embed/5c797630-f4d3-4229-8ac4-f81c148a6256',
           'id': 1,
           'isLive': False,
           'isLocal': True,
           'language': {'id': None, 'label': 'Unknown'},
           'licence': {'id': None, 'label': 'Unknown'},
           'likes': 0,
           'name': 'BigBuckBunny',
           'nsfw': False,
           'originallyPublishedAt': None,
           'previewPath': '/lazy-static/previews/83d65f27-ac7a-4a3f-9a7e-71e0b14dd99c.jpg',
           'privacy': {'id': 1, 'label': 'Public'},
           'publishedAt': '2022-07-31T00:54:44.991Z',
           'shortUUID': 'cqiZm4MvzSkrFhb5THHRgU',
           'thumbnailPath': '/static/thumbnails/d7ce4c7e-4929-4dad-854b-0473cf567f5a.jpg',
           'updatedAt': '2022-07-31T00:54:44.991Z',
           'url': 'http://cesium.tv/videos/watch/5c797630-f4d3-4229-8ac4-f81c148a6256',
           'uuid': '5c797630-f4d3-4229-8ac4-f81c148a6256',
           'viewers': 0,
           'views': 0}]}
RSP2 = {'account': {'avatars': [],
             'banners': [],
             'createdAt': '2022-07-31T00:50:59.616Z',
             'description': None,
             'displayName': 'btimby',
             'followersCount': 0,
             'followingCount': 0,
             'host': 'cesium.tv:80',
             'hostRedundancyAllowed': False,
             'id': 3,
             'name': 'btimby',
             'updatedAt': '2022-07-31T00:50:59.619Z',
             'url': 'http://cesium.tv/accounts/btimby',
             'userId': 2},
 'blacklisted': False,
 'blacklistedReason': None,
 'category': {'id': None, 'label': 'Misc'},
 'channel': {'avatars': [],
             'banners': [],
             'createdAt': '2022-07-31T00:50:59.621Z',
             'description': None,
             'displayName': "Ben's channel",
             'followersCount': 0,
             'followingCount': 0,
             'host': 'cesium.tv:80',
             'hostRedundancyAllowed': False,
             'id': 2,
             'isLocal': True,
             'name': 'btimby_channel',
             'ownerAccount': {'avatars': [],
                              'banners': [],
                              'createdAt': '2022-07-31T00:50:59.616Z',
                              'description': None,
                              'displayName': 'btimby',
                              'followersCount': 0,
                              'followingCount': 0,
                              'host': 'cesium.tv:80',
                              'hostRedundancyAllowed': False,
                              'id': 3,
                              'name': 'btimby',
                              'updatedAt': '2022-07-31T00:50:59.619Z',
                              'url': 'http://cesium.tv/accounts/btimby',
                              'userId': 2},
             'support': None,
             'updatedAt': '2022-07-31T01:01:58.517Z',
             'url': 'http://cesium.tv/video-channels/btimby_channel'},
 'commentsEnabled': True,
 'createdAt': '2022-07-31T00:55:09.068Z',
 'description': 'The first Blender Open Movie from 2006',
 'descriptionPath': '/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/description',
 'dislikes': 0,
 'downloadEnabled': True,
 'duration': 654,
 'embedPath': '/videos/embed/90222ccf-0d6d-43b4-ac4b-29f5da46119c',
 'files': [{'fileDownloadUrl': 'http://cesium.tv/download/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-720.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/04f56e6b-027d-411f-ac8d-7871d66f7863-720.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F4f7dbaa6-0de7-46f7-ad53-3890fba272e0-720.torrent&xt=urn:btih:3e2e5453d90f5b236fa5c88719b194c178b71e32&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2F04f56e6b-027d-411f-ac8d-7871d66f7863-720.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/3',
            'resolution': {'id': 720, 'label': '720p'},
            'size': 169796471,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/4f7dbaa6-0de7-46f7-ad53-3890fba272e0-720.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/4f7dbaa6-0de7-46f7-ad53-3890fba272e0-720.torrent'},
           {'fileDownloadUrl': 'http://cesium.tv/download/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-480.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/0706db2f-7fda-406c-961b-8abe91921115-480.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2Fe338f688-7f52-4402-80f2-a332ad08aefb-480.torrent&xt=urn:btih:f740ce432b223cb2a1dc8fccb08ab2d63985614f&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2F0706db2f-7fda-406c-961b-8abe91921115-480.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/17',
            'resolution': {'id': 480, 'label': '480p'},
            'size': 68562579,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/e338f688-7f52-4402-80f2-a332ad08aefb-480.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/e338f688-7f52-4402-80f2-a332ad08aefb-480.torrent'},
           {'fileDownloadUrl': 'http://cesium.tv/download/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-360.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/facbfa69-9368-4b83-ab6e-1718d10be083-360.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F383580b8-75d7-4021-8bab-e4fc900d5732-360.torrent&xt=urn:btih:70bf071d025a9a8ec482ac3a4ee5948fd11fde45&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2Ffacbfa69-9368-4b83-ab6e-1718d10be083-360.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/19',
            'resolution': {'id': 360, 'label': '360p'},
            'size': 50052112,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/383580b8-75d7-4021-8bab-e4fc900d5732-360.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/383580b8-75d7-4021-8bab-e4fc900d5732-360.torrent'}],
 'id': 2,
 'isLive': False,
 'isLocal': True,
 'language': {'id': None, 'label': 'Unknown'},
 'licence': {'id': None, 'label': 'Unknown'},
 'likes': 0,
 'name': 'ElephantsDream',
 'nsfw': False,
 'originallyPublishedAt': None,
 'previewPath': '/lazy-static/previews/e783f6af-5a7d-437f-b019-522b5b9af5bb.jpg',
 'privacy': {'id': 1, 'label': 'Public'},
 'publishedAt': '2022-07-31T00:59:06.665Z',
 'shortUUID': 'iNid2sMo2cZQrJBnipxiXs',
 'state': {'id': 1, 'label': 'Published'},
 'streamingPlaylists': [{'files': [{'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-720-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/90222ccf-0d6d-43b4-ac4b-29f5da46119c/77faeb10-2107-4bbc-a929-1bf72cc23cc2-720-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2Fbe3213d5-60d9-4ed0-b6df-fee2d0a00b83-720-hls.torrent&xt=urn:btih:fe3cdd5837f70e9a400361feb4341294b3dafa2d&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F90222ccf-0d6d-43b4-ac4b-29f5da46119c%2F77faeb10-2107-4bbc-a929-1bf72cc23cc2-720-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/14',
                                    'resolution': {'id': 720, 'label': '720p'},
                                    'size': 129405275,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/be3213d5-60d9-4ed0-b6df-fee2d0a00b83-720-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/be3213d5-60d9-4ed0-b6df-fee2d0a00b83-720-hls.torrent'},
                                   {'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-480-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/90222ccf-0d6d-43b4-ac4b-29f5da46119c/24b59752-c54c-4b59-9ba7-8aa2debfaaf5-480-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F74323f3c-bb97-4eb4-971a-0a08fa883740-480-hls.torrent&xt=urn:btih:66ccc25ee12c7f7fa245bb3e738cd49feb55b928&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F90222ccf-0d6d-43b4-ac4b-29f5da46119c%2F24b59752-c54c-4b59-9ba7-8aa2debfaaf5-480-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/24',
                                    'resolution': {'id': 480, 'label': '480p'},
                                    'size': 68449705,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/74323f3c-bb97-4eb4-971a-0a08fa883740-480-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/74323f3c-bb97-4eb4-971a-0a08fa883740-480-hls.torrent'},
                                   {'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c-360-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/90222ccf-0d6d-43b4-ac4b-29f5da46119c/94204e81-b715-4122-ab4c-8d95c4044ff7-360-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F7df4ebcd-a031-43a0-b852-4447ef85df4f-360-hls.torrent&xt=urn:btih:c96a222dc37fae4a9e9901f4847a4be776f64b96&dn=ElephantsDream&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F90222ccf-0d6d-43b4-ac4b-29f5da46119c%2F94204e81-b715-4122-ab4c-8d95c4044ff7-360-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/90222ccf-0d6d-43b4-ac4b-29f5da46119c/metadata/25',
                                    'resolution': {'id': 360, 'label': '360p'},
                                    'size': 49939498,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/7df4ebcd-a031-43a0-b852-4447ef85df4f-360-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/7df4ebcd-a031-43a0-b852-4447ef85df4f-360-hls.torrent'}],
                         'id': 2,
                         'playlistUrl': 'http://cesium.tv/static/streaming-playlists/hls/90222ccf-0d6d-43b4-ac4b-29f5da46119c/657e074a-8f44-4c21-891b-7b83c6a46b34-master.m3u8',
                         'redundancies': [],
                         'segmentsSha256Url': 'http://cesium.tv/static/streaming-playlists/hls/90222ccf-0d6d-43b4-ac4b-29f5da46119c/ab22d1db-8456-48f7-9667-36e146ca3ba5-segments-sha256.json',
                         'type': 1}],
 'support': None,
 'tags': [],
 'thumbnailPath': '/static/thumbnails/cdb1f979-c288-454a-851e-f3b7b72a586f.jpg',
 'trackerUrls': ['http://cesium.tv/tracker/announce',
                 'ws://cesium.tv:80/tracker/socket'],
 'updatedAt': '2022-07-31T00:59:06.665Z',
 'url': 'http://cesium.tv/videos/watch/90222ccf-0d6d-43b4-ac4b-29f5da46119c',
 'uuid': '90222ccf-0d6d-43b4-ac4b-29f5da46119c',
 'viewers': 0,
 'views': 0,
 'waitTranscoding': True}
RSP3 = {'account': {'avatars': [],
             'banners': [],
             'createdAt': '2022-07-31T00:50:59.616Z',
             'description': None,
             'displayName': 'btimby',
             'followersCount': 0,
             'followingCount': 0,
             'host': 'cesium.tv:80',
             'hostRedundancyAllowed': False,
             'id': 3,
             'name': 'btimby',
             'updatedAt': '2022-07-31T00:50:59.619Z',
             'url': 'http://cesium.tv/accounts/btimby',
             'userId': 2},
 'blacklisted': False,
 'blacklistedReason': None,
 'category': {'id': 4, 'label': 'Art'},
 'channel': {'avatars': [],
             'banners': [],
             'createdAt': '2022-07-31T00:50:59.621Z',
             'description': None,
             'displayName': "Ben's channel",
             'followersCount': 0,
             'followingCount': 0,
             'host': 'cesium.tv:80',
             'hostRedundancyAllowed': False,
             'id': 2,
             'isLocal': True,
             'name': 'btimby_channel',
             'ownerAccount': {'avatars': [],
                              'banners': [],
                              'createdAt': '2022-07-31T00:50:59.616Z',
                              'description': None,
                              'displayName': 'btimby',
                              'followersCount': 0,
                              'followingCount': 0,
                              'host': 'cesium.tv:80',
                              'hostRedundancyAllowed': False,
                              'id': 3,
                              'name': 'btimby',
                              'updatedAt': '2022-07-31T00:50:59.619Z',
                              'url': 'http://cesium.tv/accounts/btimby',
                              'userId': 2},
             'support': None,
             'updatedAt': '2022-07-31T01:01:58.517Z',
             'url': 'http://cesium.tv/video-channels/btimby_channel'},
 'commentsEnabled': True,
 'createdAt': '2022-07-31T00:52:47.770Z',
 'description': 'Big Buck Bunny tells the story of a giant rabbit with a heart '
                'bigger than himself. When one sunny day three rodents rudely '
                "harass him, something snaps... and the rabbit ain't no bunny "
                'anymore! In the typical cartoon tradition he prepares the '
                'nasty...',
 'descriptionPath': '/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/description',
 'dislikes': 0,
 'downloadEnabled': True,
 'duration': 596,
 'embedPath': '/videos/embed/5c797630-f4d3-4229-8ac4-f81c148a6256',
 'files': [{'fileDownloadUrl': 'http://cesium.tv/download/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-720.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/34b8f15a-a7b9-4083-969e-47d561ab0606-720.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F1a32000c-680b-4b7a-acb9-d3f7259e5ea4-720.torrent&xt=urn:btih:70f4bc51f64303af65332f94366ae7476c750e2b&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2F34b8f15a-a7b9-4083-969e-47d561ab0606-720.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/1',
            'resolution': {'id': 720, 'label': '720p'},
            'size': 158176275,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/1a32000c-680b-4b7a-acb9-d3f7259e5ea4-720.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/1a32000c-680b-4b7a-acb9-d3f7259e5ea4-720.torrent'},
           {'fileDownloadUrl': 'http://cesium.tv/download/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-480.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/4a46034c-6c69-4d22-8b92-f5a3d0286968-480.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F36a13000-9b7d-41f0-80d6-e0585f1905cb-480.torrent&xt=urn:btih:fd5d4c1fa635eb0c9761182ee5a2fb32dd74024e&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2F4a46034c-6c69-4d22-8b92-f5a3d0286968-480.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/4',
            'resolution': {'id': 480, 'label': '480p'},
            'size': 64468713,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/36a13000-9b7d-41f0-80d6-e0585f1905cb-480.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/36a13000-9b7d-41f0-80d6-e0585f1905cb-480.torrent'},
           {'fileDownloadUrl': 'http://cesium.tv/download/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-360.mp4',
            'fileUrl': 'http://cesium.tv/static/webseed/e1fc9f3b-d785-436f-ac97-90d6b68615cc-360.mp4',
            'fps': 24,
            'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F5e05e0c6-2248-4c93-9bab-2b1b4147d8a9-360.torrent&xt=urn:btih:74591d3a9ef856fbb924e1b98331f813efb27053&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fwebseed%2Fe1fc9f3b-d785-436f-ac97-90d6b68615cc-360.mp4',
            'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/6',
            'resolution': {'id': 360, 'label': '360p'},
            'size': 46528955,
            'torrentDownloadUrl': 'http://cesium.tv/download/torrents/5e05e0c6-2248-4c93-9bab-2b1b4147d8a9-360.torrent',
            'torrentUrl': 'http://cesium.tv/lazy-static/torrents/5e05e0c6-2248-4c93-9bab-2b1b4147d8a9-360.torrent'}],
 'id': 1,
 'isLive': False,
 'isLocal': True,
 'language': {'id': None, 'label': 'Unknown'},
 'licence': {'id': None, 'label': 'Unknown'},
 'likes': 0,
 'name': 'BigBuckBunny',
 'nsfw': False,
 'originallyPublishedAt': None,
 'previewPath': '/lazy-static/previews/83d65f27-ac7a-4a3f-9a7e-71e0b14dd99c.jpg',
 'privacy': {'id': 1, 'label': 'Public'},
 'publishedAt': '2022-07-31T00:54:44.991Z',
 'shortUUID': 'cqiZm4MvzSkrFhb5THHRgU',
 'state': {'id': 1, 'label': 'Published'},
 'streamingPlaylists': [{'files': [{'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-720-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/5c797630-f4d3-4229-8ac4-f81c148a6256/341d70b2-0d9b-4186-b950-4f03ac3e6cf0-720-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2F50e58f2a-77f6-4d35-9079-a7316080e62d-720-hls.torrent&xt=urn:btih:171b2b9fc811867f1a4a68080f09ebcd7112260f&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F5c797630-f4d3-4229-8ac4-f81c148a6256%2F341d70b2-0d9b-4186-b950-4f03ac3e6cf0-720-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/2',
                                    'resolution': {'id': 720, 'label': '720p'},
                                    'size': 120517078,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/50e58f2a-77f6-4d35-9079-a7316080e62d-720-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/50e58f2a-77f6-4d35-9079-a7316080e62d-720-hls.torrent'},
                                   {'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-480-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/5c797630-f4d3-4229-8ac4-f81c148a6256/41ce645f-91ed-4ad2-8e64-8130527918bd-480-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2Fd9bc6557-ced6-470a-94c2-4263d727f880-480-hls.torrent&xt=urn:btih:71d89aa9b9767717dbe75a422c7246679780a2cb&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F5c797630-f4d3-4229-8ac4-f81c148a6256%2F41ce645f-91ed-4ad2-8e64-8130527918bd-480-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/7',
                                    'resolution': {'id': 480, 'label': '480p'},
                                    'size': 64358375,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/d9bc6557-ced6-470a-94c2-4263d727f880-480-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/d9bc6557-ced6-470a-94c2-4263d727f880-480-hls.torrent'},
                                   {'fileDownloadUrl': 'http://cesium.tv/download/streaming-playlists/hls/videos/5c797630-f4d3-4229-8ac4-f81c148a6256-360-fragmented.mp4',
                                    'fileUrl': 'http://cesium.tv/static/streaming-playlists/hls/5c797630-f4d3-4229-8ac4-f81c148a6256/3bbf6882-ce00-4746-a391-8165aac7ab1e-360-fragmented.mp4',
                                    'fps': 24,
                                    'magnetUri': 'magnet:?xs=http%3A%2F%2Fcesium.tv%2Flazy-static%2Ftorrents%2Fd497e7b7-5f2b-4b68-8b3a-7002e5dd7139-360-hls.torrent&xt=urn:btih:2e9206ef8e600936effac3d3f13ae888af7f41fe&dn=BigBuckBunny&tr=http%3A%2F%2Fcesium.tv%2Ftracker%2Fannounce&tr=ws%3A%2F%2Fcesium.tv%3A80%2Ftracker%2Fsocket&ws=http%3A%2F%2Fcesium.tv%2Fstatic%2Fstreaming-playlists%2Fhls%2F5c797630-f4d3-4229-8ac4-f81c148a6256%2F3bbf6882-ce00-4746-a391-8165aac7ab1e-360-fragmented.mp4',
                                    'metadataUrl': 'http://cesium.tv/api/v1/videos/5c797630-f4d3-4229-8ac4-f81c148a6256/metadata/8',
                                    'resolution': {'id': 360, 'label': '360p'},
                                    'size': 46428213,
                                    'torrentDownloadUrl': 'http://cesium.tv/download/torrents/d497e7b7-5f2b-4b68-8b3a-7002e5dd7139-360-hls.torrent',
                                    'torrentUrl': 'http://cesium.tv/lazy-static/torrents/d497e7b7-5f2b-4b68-8b3a-7002e5dd7139-360-hls.torrent'}],
                         'id': 1,
                         'playlistUrl': 'http://cesium.tv/static/streaming-playlists/hls/5c797630-f4d3-4229-8ac4-f81c148a6256/242d2b40-ced3-4eab-b76a-0bbf238e752c-master.m3u8',
                         'redundancies': [],
                         'segmentsSha256Url': 'http://cesium.tv/static/streaming-playlists/hls/5c797630-f4d3-4229-8ac4-f81c148a6256/4d565ae7-2c1e-475c-8bcb-5802415fff80-segments-sha256.json',
                         'type': 1}],
 'support': None,
 'tags': [],
 'thumbnailPath': '/static/thumbnails/d7ce4c7e-4929-4dad-854b-0473cf567f5a.jpg',
 'trackerUrls': ['http://cesium.tv/tracker/announce',
                 'ws://cesium.tv:80/tracker/socket'],
 'updatedAt': '2022-07-31T00:54:44.991Z',
 'url': 'http://cesium.tv/videos/watch/5c797630-f4d3-4229-8ac4-f81c148a6256',
 'uuid': '5c797630-f4d3-4229-8ac4-f81c148a6256',
 'viewers': 0,
 'views': 0,
 'waitTranscoding': True}


class PeerTubTestCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = ResponsesServer(
            responses_kwargs={'registry': OrderedRegistry})
        self.server.start()
        self.crawler = PeerTubeCrawler()
        self.server.get(
            self.server.url('/api/v1/video-channels/btimby_channel@cesium.tv:80'),
            json=RSP0)
        self.server.get(
            self.server.url('/api/v1/video-channels/btimby_channel@cesium.tv:80/videos'),
            json=RSP1)
        self.server.get(
            self.server.url('/api/v1/videos/iNid2sMo2cZQrJBnipxiXs'), json=RSP2)
        self.server.get(
            self.server.url('/api/v1/videos/cqiZm4MvzSkrFhb5THHRgU'), json=RSP3)

    def tearDown(self):
        self.server.stop()

    async def test_login(self):
        pass #  await self.crawler.login()

    async def test_peertube(self):
        channel, videos = await self.crawler.crawl(self.server.url('/c/btimby_channel@cesium.tv:80'))
        videos = [v async for v, s in videos]
        self.assertEqual('btimby_channel@cesium.tv:80', channel.name)
        self.assertEqual(2, len(videos))
        self.assertEqual('ElephantsDream',videos[0].title)
        self.assertEqual(3, len(videos[0].sources))
        self.assertEqual(
            'http://cesium.tv/static/webseed/04f56e6b-027d-411f-ac8d-7871d66f7863-720.mp4',
            videos[0].sources[0].url)