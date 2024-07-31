import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    // Enter test mode
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    const job = queue.testMode.jobs[0];
    expect(job.type).to.equal('push_notification_code_3');
    expect(job.data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });

    const job2 = queue.testMode.jobs[1];
    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.eql({
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    });
  });

  it('should log the correct messages', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    const logSpy = sinon.spy(console, 'log');

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].emit('complete');
    queue.testMode.jobs[0].emit('failed', new Error('Error message'));
    queue.testMode.jobs[0].emit('progress', 50);

    setTimeout(() => {
      expect(logSpy.calledWith('Notification job created: 1')).to.be.true;
      expect(logSpy.calledWith('Notification job 1 completed')).to.be.true;
      expect(logSpy.calledWith('Notification job 1 failed: Error message')).to.be.true;
      expect(logSpy.calledWith('Notification job 1 50% complete')).to.be.true;

      logSpy.restore();
      done();
    }, 100);
  });
});

