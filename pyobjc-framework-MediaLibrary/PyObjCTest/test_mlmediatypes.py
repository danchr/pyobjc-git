import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MediaLibrary

    class TestMLMediaTypes(TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MediaLibrary.MLMediaSourceTypeAudio, 1)
            self.assertEqual(MediaLibrary.MLMediaSourceTypeImage, 2)
            self.assertEqual(MediaLibrary.MLMediaSourceTypeMovie, 4)

            self.assertEqual(MediaLibrary.MLMediaTypeAudio, 1)
            self.assertEqual(MediaLibrary.MLMediaTypeImage, 2)
            self.assertEqual(MediaLibrary.MLMediaTypeMovie, 4)

            self.assertIsInstance(MediaLibrary.MLFolderRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLFolderGroupTypeIdentifier, unicode)

            self.assertIsInstance(MediaLibrary.MLiTunesRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLiTunesPlaylistTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLiTunesPurchasedPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesPodcastPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesSmartPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesFolderPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesMoviesPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesTVShowsPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesAudioBooksPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesMusicPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesGeniusPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesSavedGeniusPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesiTunesUPlaylistTypeIdentifier, unicode
            )

            self.assertIsInstance(MediaLibrary.MLiPhotoRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLiPhotoAlbumTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLiPhotoLibraryAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoEventsFolderTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoSmartAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoEventAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoLastImportAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoLastNMonthsAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFlaggedAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFolderAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoSubscribedAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFacesAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPlacesAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPlacesCountryAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPlacesProvinceAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPlacesCityAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFacebookAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFlickrAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFacebookGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoFlickrGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoSlideShowAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoLastViewedEventAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiPhotoPhotoStreamAlbumTypeIdentifier, unicode
            )

            self.assertIsInstance(
                MediaLibrary.MLApertureRootGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureUserAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureUserSmartAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureProjectAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFolderAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureProjectFolderAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureLightTableTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFlickrGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFlickrAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFacebookGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFacebookAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureSmugMugGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureSmugMugAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureSlideShowTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureAllPhotosTypeIdentifier, unicode
            )
            self.assertIsInstance(MediaLibrary.MLApertureFlaggedTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLApertureAllProjectsTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureFacesAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePlacesAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePlacesCountryAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePlacesProvinceAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePlacesCityAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePlacesPointOfInterestAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureLastImportAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureLastNMonthsAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLApertureLastViewedEventAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLAperturePhotoStreamAlbumTypeIdentifier, unicode
            )

            self.assertIsInstance(
                MediaLibrary.MLGarageBandRootGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLGarageBandFolderGroupTypeIdentifier, unicode
            )

            self.assertIsInstance(MediaLibrary.MLLogicRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLLogicBouncesGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLLogicProjectsGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(MediaLibrary.MLLogicProjectTypeIdentifier, unicode)

            self.assertIsInstance(MediaLibrary.MLiMovieRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLiMovieEventGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiMovieProjectGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiMovieEventLibraryGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiMovieEventCalendarGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiMovieFolderGroupTypeIdentifier, unicode
            )

            self.assertIsInstance(
                MediaLibrary.MLFinalCutRootGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLFinalCutEventGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLFinalCutProjectGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLFinalCutEventLibraryGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLFinalCutEventCalendarGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLFinalCutFolderGroupTypeIdentifier, unicode
            )

            self.assertIsInstance(MediaLibrary.MLMediaObjectDurationKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectArtistKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectAlbumKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectGenreKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectKindKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectTrackNumberKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectBitRateKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectSampleRateKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectChannelCountKey, unicode)
            self.assertIsInstance(
                MediaLibrary.MLMediaObjectResolutionStringKey, unicode
            )
            self.assertIsInstance(MediaLibrary.MLMediaObjectCommentsKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectKeywordsKey, unicode)
            self.assertIsInstance(MediaLibrary.MLMediaObjectProtectedKey, unicode)

        @min_os_level("10.10")
        def testConstants10_10(self):
            self.assertIsInstance(
                MediaLibrary.MLiTunesMusicVideosPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLiTunesVideoPlaylistTypeIdentifier, unicode
            )
            self.assertIsInstance(MediaLibrary.MLPhotosRootGroupTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLPhotosSharedGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAlbumsGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(MediaLibrary.MLPhotosAlbumTypeIdentifier, unicode)
            self.assertIsInstance(MediaLibrary.MLPhotosFolderTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLPhotosSmartAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosPublishedAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAllMomentsGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosMomentGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAllCollectionsGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosCollectionGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAllYearsGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(MediaLibrary.MLPhotosYearGroupTypeIdentifier, unicode)
            self.assertIsInstance(
                MediaLibrary.MLPhotosLastImportGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosMyPhotoStreamTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosSharedPhotoStreamTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosFavoritesGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosPanoramasGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosVideosGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosSloMoGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosTimelapseGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosBurstGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosFacesAlbumTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAllPhotosAlbumTypeIdentifier, unicode
            )

        @min_os_level("10.11")
        def testConstants10_11(self):
            self.assertIsInstance(
                MediaLibrary.MLPhotosFrontCameraGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosScreenshotGroupTypeIdentifier, unicode
            )

        @min_os_level("10.12")
        def testConstants10_12(self):
            self.assertIsInstance(
                MediaLibrary.MLPhotosDepthEffectGroupTypeIdentifier, unicode
            )

        @min_os_level("10.13")
        def testConstants10_13(self):
            self.assertIsInstance(
                MediaLibrary.MLPhotosLivePhotosGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosLongExposureGroupTypeIdentifier, unicode
            )
            self.assertIsInstance(
                MediaLibrary.MLPhotosAnimatedGroupTypeIdentifier, unicode
            )


if __name__ == "__main__":
    main()
