/**
 *
 * --------------------------------------------------------------------
 *
 * Template : Custom Js Template
 * Author : reacthemes
 * Author URI : http://www.reactheme.com/
 *
 * --------------------------------------------------------------------
 *
 **/
(function ($) {
    "use strict";

    $(document).ready(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    $.fn.skillBars = function (options) {
        var settings = $.extend({
            from: 0, // number start
            to: false, // number end
            speed: 1000, // how long it should take to count between the target numbers
            interval: 100, // how often the element should be updated
            decimals: 0, // the number of decimal places to show
            onUpdate: null, // callback method for every time the element is updated,
            onComplete: null, // callback method for when the element finishes updating
            /*onComplete: function(from) {
                console.debug(this);
            }*/
            classes: {
                skillBarBar: '.skillbar-bar',
                skillBarPercent: '.skill-bar-percent',
            }
        }, options);

        return this.each(function () {

            var obj = $(this),
                to = (settings.to != false) ? settings.to : parseInt(obj.attr('data-percent'));
            if (to > 100) {
                to = 100;
            };
            var from = settings.from,
                loops = Math.ceil(settings.speed / settings.interval),
                increment = (to - from) / loops,
                loopCount = 0,
                interval = setInterval(updateValue, settings.interval);

            obj.find(settings.classes.skillBarBar).animate({
                width: parseInt(obj.attr('data-percent')) + '%'
            }, settings.speed);

            function updateValue() {
                from += increment;
                loopCount++;
                $(obj).find(settings.classes.skillBarPercent).text(from.toFixed(settings.decimals) + '%');

                if (typeof (settings.onUpdate) == 'function') {
                    settings.onUpdate.call(obj, from);
                }

                if (loopCount >= loops) {
                    clearInterval(interval);
                    from = to;

                    if (typeof (settings.onComplete) == 'function') {
                        settings.onComplete.call(obj, from);
                    }
                }
            }
        });
    };
    // Cart show & hide
    $(document).on('click', '.menu-cart-area', function () {
        $(".cart-icon-total-products").addClass("visible-cart");
        $(".body-overlay-cart").addClass("overlayshow");
    });
    $(document).on('click', '.body-overlay-cart', function () {
        $(this).removeClass("overlayshow");
        $(".cart-icon-total-products").removeClass("visible-cart");
    });

    $(document).on('click', '.close-cart', function () {
        $(".cart-icon-total-products").removeClass("visible-cart");
        $(".body-overlay-cart").removeClass("overlayshow");
    });    

    document.addEventListener("DOMContentLoaded", function() {
        const circleText = document.querySelector('.circle-text');
        if (circleText) {
            const textSpans = circleText.querySelectorAll('span');
            let rotation = 0;
            const rotationStep = 360 / textSpans.length;
    
            textSpans.forEach((span, index) => {
                span.style.transform = `rotate(${rotation}deg) translateX(150px)`;
                rotation += rotationStep;
            });
        }
    });

    window.addEventListener('load', function() {
        // Wait for all images to be loaded
        $('.rts-filter').imagesLoaded(function() {
            // Isotope initialization
            var $grid = $('.rts-filter').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry: {
                    columnWidth: '.grid-item',
                },
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });    
            
            // Click event for filter buttons
            $('.portfolio-filter button').on('click', function(event) {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({
                    filter: filterValue
                });
    
                // Set the 'active' class to the clicked button
                $(this).siblings('.active').removeClass('active');
                $(this).addClass('active');
    
                event.preventDefault();
            });
        });
    });
    
})(jQuery);