// Standard console logs
console.log('This is a standard log.'); // Regular log
console.info('This is an informational log.'); // Information log
console.warn('This is a warning log.'); // Warning log
console.error('This is an error log.'); // Error log

// Custom logs with formatting
console.log('%cStyled log', 'color: blue; font-weight: bold;'); // Custom styled log

// Grouping logs
console.group('Grouped logs');
console.log('Log 1');
console.log('Log 2');
console.log('Log 3');
console.groupEnd();
