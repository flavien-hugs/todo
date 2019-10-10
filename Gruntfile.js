// configuration du projet grunt

'use strict';
module.exports = function(grunt) {
  // Ici, toutes les configurations
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // configuration du plugin grunt-contrib-concat.
    concat: {
      options: {
        stripBanners: true,
        banner: '/*!<%=pkg.name%> - v<%= pkg.version%> - ' +
          '<%= grunt.template.today("yyyy-mm-dd") %> */',
      },

      dist: {
        src: [
          // lister tous les fichiers js dans tasks dans app.js
          'tasks/static/tasks/js/*.js',
          'tasks/static/tasks/js/script.js'
        ],
        dest: 'tasks/static/tasks/js/vendor/script.min.js'
      }
    },

    // configuration du plugin grunt-contrib-uglify.
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
          '<%= grunt.template.today("yyyy-mm-dd") %> */',
        // evite de modifier les noms des variables
        mangle: false,
        sourceMap: true,
        sourceMapName: 'tasks/static/tasks/vendor/js/script.map',
        drop_console: true,
        beautify: true
      },

      built: {
        src: 'tasks/static/tasks/vendor/js/script.js',
        dest: 'tasks/static/tasks/vendor/js/script.min.js'
      }
    },

    // configuration du plugin grunt-contrib-imagemin
    imagemin: {
      dynamic: {
        files: [{
          expand: true,
          cwd: 'tasks/static/tasks/img/',
          src: ['**/*.{png,jpg,gif}'],
          dest: 'tasks/static/tasks/vendor/img/'
        }]
      }
    },

    // configuration du plugin grunt-contrib-sass
    sass: {
      dist: {
        options: {
          style: 'compressed'
        },
        files: [{
          expand: true,
          cwd: 'tasks/static/tasks/css/',
          src: ['*.css'],
          dest: 'tasks/static/tasks/vendor/css/',
          ext: '.min.css'
        }]
      }
    },

    // configuration du plugin grunt-contrib-watch
    watch: {
      scripts: {
        files: ['**/*.js'],
        tasks: ['concat', 'uglify'],
        options: {
          spawn: false,
          interrupt: true,
          debounceDelay: 250,
          livereload: {
            host: 'localhost',
            port: 8000,
          }
        },
      },

      sass: {
        files: ['**/*.scss'],
        tasks: ['sass'],
        options: {
          spawn: false,
        }
      }
    }

  });

  // dire à grunt de l'utilisation du plugin
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-django');

  grunt.registerTask('default', ['concat', 'uglify', 'imagemin', 'sass', 'watch']);

}
