if (new URLSearchParams(location.search).has('dark')) document.body.classList.add('dark');

document.querySelectorAll('details pre').forEach((pre, index) => {
  const block = document.createElement('div');
  block.className = 'prompt-block';
  pre.before(block);
  const toolbar = document.createElement('div');
  toolbar.className = 'prompt-toolbar';
  const status = document.createElement('span');
  status.className = 'copy-status';
  status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite');
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'copy-button';
  button.textContent = 'Copy';
  button.setAttribute('aria-label', index === 0 ? 'Copy new project prompt' : 'Copy existing codebase prompt');
  toolbar.append(status, button);
  block.append(toolbar, pre);
  let resetTimer;
  button.addEventListener('click', async () => {
    clearTimeout(resetTimer);
    status.textContent = '';
    button.disabled = true;
    button.textContent = 'Copying…';
    try {
      await navigator.clipboard.writeText(pre.textContent.replace(/\n$/, ''));
      button.textContent = 'Copied!';
      status.textContent = 'Prompt copied.';
    } catch {
      button.textContent = 'Copy';
      status.textContent = 'Could not copy. Select the prompt and copy manually.';
    } finally {
      button.disabled = false;
    }
    resetTimer = setTimeout(() => { button.textContent = 'Copy'; status.textContent = ''; }, 3000);
  });
});
