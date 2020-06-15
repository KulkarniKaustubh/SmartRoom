package com.example.opencvfacerec

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.SurfaceView
import androidx.appcompat.app.AppCompatActivity
import org.opencv.android.*
import org.opencv.core.*
import org.opencv.android.JavaCameraView
import org.opencv.imgproc.Imgproc
import org.opencv.objdetect.CascadeClassifier
import java.io.File
import java.io.FileOutputStream


class MainActivity : AppCompatActivity(), CameraBridgeViewBase.CvCameraViewListener2 {

    var javaCamView : JavaCameraView? = null
    lateinit var cascadeFile : File
    var faceDetector: CascadeClassifier? = null
    lateinit var mRgba : Mat
    lateinit var mGray : Mat

    private var baseLoaderCallback = object : BaseLoaderCallback(this) {

        override fun onManagerConnected(status: Int) {

            when (status) {
                LoaderCallbackInterface.SUCCESS -> {
//                    var inputStream = resources.openRawResource(R.raw.haarcascade_frontalface_alt2)
//                    var cascadeDir = getDir("cascade", Context.MODE_PRIVATE)
//                    cascadeFile = File(cascadeDir, "haarcascades_frontalface_alt2.xml")
//
//                    var fos = FileOutputStream(cascadeFile)
//
//                    var buffer : ByteArray = ByteArray(4096)
//                    var bytesRead : Int
//                    bytesRead = inputStream.read(buffer)
//
//                    while (bytesRead != -1) {
//                        fos.write(buffer, 0, bytesRead)
//                        bytesRead = inputStream.read(buffer)
//                    }
//
//                    inputStream.close()
//                    fos.close()
//
//                    faceDetector = CascadeClassifier(cascadeFile.absolutePath)
//
//                    if (faceDetector?.empty()!!) {
//                        faceDetector = null
//                    } else {
//                        cascadeDir.delete()
//                    }
                    Log.d("Baseloader", "in baseloader")
                    javaCamView?.enableView()
                }
                else -> {
                    super.onManagerConnected(status)
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("MainActivity", "In on create main act")

        javaCamView = findViewById<JavaCameraView>(R.id.java_camera_view)
        javaCamView?.visibility = SurfaceView.VISIBLE
        javaCamView?.setCvCameraViewListener(this)

        if (!OpenCVLoader.initDebug()) {
            Log.d("MainActivity", "opencv failed")
            OpenCVLoader.initAsync(OpenCVLoader.OPENCV_VERSION, this, baseLoaderCallback)
        } else {
            Log.d("MainActivity", "opencv success")
            baseLoaderCallback.onManagerConnected(LoaderCallbackInterface.SUCCESS)
        }
    }


    override fun onCameraViewStarted(width: Int, height: Int) {
        Log.d("Camera", "Camera view started")
        mRgba = Mat(height, width, CvType.CV_8UC4)
        mGray = Mat(width, width, CvType.CV_8UC4);
//        mGray = Mat()
    }

    override fun onCameraViewStopped() {
        Log.d("Camera", "Camera view stopped")
        mRgba.release()
        mGray.release()
    }

    override fun onCameraFrame(inputFrame: CameraBridgeViewBase.CvCameraViewFrame?): Mat {
        Log.d("Camera", "In camera frame")
        mRgba = inputFrame?.rgba()!!
        mGray = mRgba.t()
        Core.flip(mRgba.t(), mGray, 1)
        Imgproc.resize(mGray, mGray, mRgba.size())
        return mGray
//        mGray = inputFrame?.gray()!!

//        var faceDetections = MatOfRect()
//
//        faceDetector?.detectMultiScale(mRgba, faceDetections)
//
//        for (rect in faceDetections.toArray()) {
//
//            val pt1 = Point(rect.x.toDouble(), rect.y.toDouble())
//            val pt2 = Point (rect.x.toDouble() + rect.width.toDouble(), rect.y.toDouble() + rect.height.toDouble())
//
//            Imgproc.rectangle(mRgba, pt1, pt2, Scalar(255.0, 0.0, 0.0))
//        }
//
//        return mRgba
    }

    override fun onDestroy() {
        super.onDestroy()
        javaCamView?.disableView()
    }

    override fun onPause() {
        super.onPause()
        javaCamView?.disableView()
    }

    override fun onResume() {
        super.onResume()

        if (OpenCVLoader.initDebug()) {
            baseLoaderCallback.onManagerConnected(BaseLoaderCallback.SUCCESS)
        } else {
            OpenCVLoader.initAsync(OpenCVLoader.OPENCV_VERSION, this, baseLoaderCallback)
        }
    }
}
