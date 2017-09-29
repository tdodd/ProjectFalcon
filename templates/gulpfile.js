/**
 * Gulp Dependencies
 */
const gulp = require('gulp');
const imagemin = require('gulp-imagemin');
const sass = require('gulp-sass');
const concat = require('gulp-concat');
const babel = require('gulp-babel');
const uglify = require('gulp-uglify');
const htmlmin = require('gulp-htmlmin');
const browserSync = require('browser-sync').create();
const rename = require("gulp-rename");
const sourcemaps = require('gulp-sourcemaps');

/**
 * Location Constants
 */

// Inputs
const sassIn = 'app/**/*.sass';
const es6In = 'public/javascripts/*.js';
const imagesIn = 'public/images/**/*';
const views = 'app/**/*.pug';

// Outputs
const sassOut = 'public/stylesheets';
const es6Out = 'public/javascripts';
const imagesOut = 'public/assets/images';

/**
 * Tasks
 */

// Compile, minify and concatenate sass files
gulp.task('compile-sass', () => {
	gulp.src(sassIn)
		.pipe(sass({ outputStyle: 'compressed' }))
		.pipe(concat('styles.css'))
		.pipe(gulp.dest(sassOut))
		.pipe(browserSync.stream());
});

// Compile, minify and concatenate es6 files
gulp.task('compile-es6', () => {
	gulp.src([es6In, '!' + es6Out + '/main.js']) // Don't recompile bundle
		.pipe(sourcemaps.init())
		.pipe(babel({ presets: ['es2015'] }))
		.pipe(uglify())
		.pipe(concat('main.js'))
		.pipe(sourcemaps.write())
		.pipe(gulp.dest(es6Out))
		.pipe(browserSync.stream());
});

// Optimize images
gulp.task('minify-images', () => {
	gulp.src(imagesIn)
		.pipe(imagemin())
		.pipe(gulp.dest(imagesOut))
		.pipe(browserSync.stream());
});

// Monitor files for changes
gulp.task('watch-files', () => {
	browserSync.init({
		proxy: 'localhost:3000'
	});
	gulp.watch(sassIn, ['compile-sass']);
	gulp.watch(es6In, ['compile-es6']);
	gulp.watch(imagesIn, ['minify-images']);
	gulp.watch(views).on('change', browserSync.reload);
});

// Compile and output to build directory
gulp.task('build', ['compile-sass', 'compile-es6', 'minify-images']);

// Default task
gulp.task('default', ['watch-files']);
